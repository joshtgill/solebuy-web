from django.shortcuts import render
from solebuy.forms import CategoryForm
from .forms import FilterForm
from .models import *
from buyer.src.assistant import Assistant


def home(request):
    # Get all category names
    categoryNames = [category.name for category in Category.objects.all()]

    # Build content for template
    content = {'categoryForm': CategoryForm(), 'categoryNames': categoryNames}

    return render(request, 'home.html', content)


def category(request):
    # Get the incoming category name
    categoryName = ''
    categoryForm = CategoryForm(request.GET)
    if categoryForm.is_valid():
        categoryName = categoryForm.cleaned_data['name']
    else:
        return render(request, 'category.html')

    # Attempt to get category object from name
    category = None
    try:
        category = Category.objects.get(name=categoryName)
    except:
        content = {'categoryForm': categoryForm, 'filtersWidth': str(50), 'filterWidth': '100%'}
        return render(request, 'category.html', content)

    # Respond to the request
    if request.method == 'POST':
        # Filter form submited. Update ID map with selection
        filterForm = FilterForm(request.POST)
        if filterForm.is_valid():
            updateIdMap(request, filterForm.cleaned_data.get('button'))
    else:
        resetIdMap(request, len(Assister.objects.filter(category=category)))

    # Find recommended products based on AF selections
    filteredProducts = Assistant().filterProducts(Product.objects.filter(category=category),
                                                  request.session['userAFIds']).get('primary')
    filteredProducts = sorted(filteredProducts, key=lambda product: product.price)

    # Build content for template
    content = {'categoryForm': categoryForm, 'categoryData': serializeCategory(category, filteredProducts),
               'userAFIds': request.session['userAFIds'], 'filteredProducts': filteredProducts}

    return render(request, 'category.html', content)


def updateIdMap(request, selectValue):
    assisterId = int(selectValue[ : selectValue.find('.')])
    filterId = int(selectValue[selectValue.find('.') + 1 : ])
    userAFIds = request.session['userAFIds']
    if filterId not in userAFIds[assisterId]:
        userAFIds[assisterId].append(filterId)
    else:
        userAFIds[assisterId].remove(filterId)

    request.session['userAFIds'] = userAFIds


def resetIdMap(request, numAssisters):
    request.session['userAFIds'] = [[] for i in range(numAssisters)]


def serializeCategory(category, filteredProducts):
    # Category data
    categoryData = {'name': category.name, 'assisters': [], 'filteredProducts': []}

    # Assister data
    for assister in Assister.objects.filter(category=category):
        assisterData = {'name': assister.name, 'prompt': assister.prompt,
                        'filters': [filterr.contents for filterr in Filter.objects.filter(assister=assister)]}
        categoryData.get('assisters').append(assisterData)

    # Product data
    for product in filteredProducts:
        categoryData.get('filteredProducts').append(serializeProduct(product))

    return categoryData


def serializeProduct(product, serializeProcons=True):
    productData = {'id': product.id, 'name': product.name, 'price': product.price,
                   'imageFileName': product.imageFileName, 'prosSummary': product.prosSummary,
                   'consSummary': product.consSummary, 'pros': [], 'cons': []}

    if serializeProcons:
        for pro in Pro.objects.filter(product=product):
            productData.get('pros').append(pro.contents)

        for con in Con.objects.filter(product=product):
            productData.get('cons').append(con.contents)

    return productData
