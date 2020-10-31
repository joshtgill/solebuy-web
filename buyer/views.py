from django.shortcuts import render
from solebuy.forms import CategoryForm
from .forms import FilterForm, ProductForm
from .models import Category
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
    popupProduct = None
    if request.method == 'POST':
        # Filter form submited. Update ID map with selection
        filterForm = FilterForm(request.POST)
        if filterForm.is_valid():
            updateIdMap(request, filterForm.cleaned_data.get('button'))

        # Product form submitted. Get product data for popup
        productForm = ProductForm(request.POST)
        if productForm.is_valid():
            popupProduct = category.products.all().get(id=productForm.cleaned_data['idd'])
    else:
        popupProduct = None
        resetIdMap(request, len(category.assisters.all()))

    # Find recommended products based on AF selections
    filteredProducts = Assistant().filterProducts(category.products.all(),
                                             request.session['AFIdMap']).get('primary')
    filteredProducts = sorted(filteredProducts, key=lambda product: product.price)

    # Build content for template
    content = {'categoryForm': categoryForm, 'category': category,
               'AFIdMap': request.session['AFIdMap'],
               'filteredProducts': filteredProducts, 'popupProduct': popupProduct}

    return render(request, 'category.html', content)


def updateIdMap(request, selectValue):
    assisterId = int(selectValue[ : selectValue.find('.')])
    filterId = int(selectValue[selectValue.find('.') + 1 : ])
    AFIdMap = request.session['AFIdMap']
    if filterId not in AFIdMap[assisterId]:
        AFIdMap[assisterId].append(filterId)
    else:
        AFIdMap[assisterId].remove(filterId)

    request.session['AFIdMap'] = AFIdMap


def resetIdMap(request, numAssisters):
    request.session['AFIdMap'] = [[] for i in range(numAssisters)]
