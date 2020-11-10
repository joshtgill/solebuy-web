from django.shortcuts import render
from solebuy.forms import CategoryForm
from .forms import FilterForm
from .models import *
from buyer.src.assistant import Assistant
from datetime import datetime


def home(request):
    # Get all category names
    categoryNames = [category.name for category in Category.objects.all()]

    # Build content for template
    content = {'categoryForm': CategoryForm(), 'categoryNames': categoryNames}

    return render(request, 'home.html', content)


def category(request):
    content = {}

    # Get category from, attempt to get a category object from search
    category = None
    categoryForm = CategoryForm(request.GET)
    if categoryForm.is_valid():
        try:
            category = Category.objects.get(name=categoryForm.cleaned_data['name'])
        except:
            return render(request, 'category.html', {'categoryForm': categoryForm})
    else:
        return render(request, 'category.html')
    content.update({'categoryForm': categoryForm, 'category': category})

    # Get the category's products and serialized assisters
    products = Product.objects.filter(category=category)
    assistersData = serializeAssisters(category)
    content.update({'assistersData': assistersData})

    # Respond based on request
    if request.method == 'GET':
        content.update({'userAFIds': resetIdMap(request, len(assistersData)),
                        'filteredProducts': serializeProducts(products)})
    else:
        # Update AF IDs with selection from form
        filterForm = FilterForm(request.POST)
        if filterForm.is_valid():
            userAFIds = updateIdMap(request, filterForm.cleaned_data.get('button'), assistersData)
            content.update({'userAFIds': userAFIds})

        # Find recommended products based on AF IDs selected
        filteredProducts = Assistant().filterProducts(products, userAFIds).get('primary')
        content.update({'filteredProducts': serializeProducts(sorted(filteredProducts,
                                                                     key=lambda product: product.price))})

    return render(request, 'category.html', content)


def updateIdMap(request, selectValue, assistersData):
    assisterId = int(selectValue[ : selectValue.find('.')])
    filterId = int(selectValue[selectValue.find('.') + 1 : ])
    userAFIds = request.session['userAFIds']
    if filterId not in userAFIds[assisterId]:
        # If Assister is decisive, only allow a single filter to be selected at a time
        if assistersData[assisterId].get('object').decisive:
            userAFIds[assisterId].clear()

        userAFIds[assisterId].append(filterId)
    else:
        userAFIds[assisterId].remove(filterId)

    request.session['userAFIds'] = userAFIds

    return userAFIds


def resetIdMap(request, numAssisters):
    userAFIds = [[] for i in range(numAssisters)]
    request.session['userAFIds'] = userAFIds

    return userAFIds


def serializeAssisters(category):
    assistersData = []
    for assister in Assister.objects.filter(category=category):
        assisterData = {'object': assister,
                        'filters': [filterr.contents for filterr in Filter.objects.filter(assister=assister)]}
        assistersData.append(assisterData)

    return assistersData


def serializeProducts(products):
    productsData = []
    # Pro and Con objects are not manually serialized for efficiency
    for product in products:
        productsData.append({'data': {'id': product.id, 'name': product.name, 'price': product.price,
                                      'imageFileName': product.imageFileName, 'prosSummary': product.prosSummary,
                                      'consSummary': product.consSummary},
                             'pros': Pro.objects.filter(product=product), 'cons': Con.objects.filter(product=product)})

    return productsData
