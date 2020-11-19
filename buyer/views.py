from django.shortcuts import render
from solebuy.forms import CategoryForm
from .forms import FilterForm, SortForm
from .models import *
from buyer.src.assistant import Assistant
from datetime import datetime


def home(request):
    # Get all category names
    content = {'categoryForm': CategoryForm(),
               'categoryNames': [category.name for category in Category.objects.all()]}

    return render(request, 'home.html', content)


def category(request):
    content = {}

    # Attempt to get category object from form
    formCategoryName = ''
    category = None
    categoryForm = CategoryForm(request.GET)
    if categoryForm.is_valid():
        try:
            formCategoryName = categoryForm.cleaned_data['name'].lower().capitalize()
            category = Category.objects.get(name=formCategoryName)
            content.update({'categoryForm': CategoryForm({'name': formCategoryName})})
        except:
            pass

    if not category:
        return render(request, 'category_not_found.html', {'categoryForm': CategoryForm(),
                                                           'formCategoryName': formCategoryName,
                                                           'categoryNames': [category.name for category in Category.objects.all()]})
    content.update({'category': category})

    # Get the category's products and serialized assisters
    products = sorted(Product.objects.filter(category=category), key=lambda product: product.ranking)
    assistersData = serializeAssisters(category)
    content.update({'assistersData': assistersData})

    # Respond to the request
    if request.method == 'GET':
        resetAFIdMap(request, len(assistersData))
        resetSortValue(request)
    else:
        if 'filterField' in request.POST:
            filterForm = FilterForm(request.POST)
            if filterForm.is_valid():
                updateAFIdMap(request, filterForm.cleaned_data.get('filterField'), assistersData)
        elif 'sortField' in request.POST:
            sortForm = SortForm(request.POST)
            if sortForm.is_valid():
                updateSortValue(request, sortForm.cleaned_data.get('sortField'))

        # Sort products accordingly
        if request.session['sortValue'] == 'PRICE_LOW':
            products = sorted(products, key=lambda product: product.price)
        elif request.session['sortValue'] == 'PRICE_HIGH':
            products = sorted(products, key=lambda product: product.price, reverse=True)

        products = Assistant().filterProducts(products, request.session['userAFIds']).get('primary')

    # Use existing AF IDs and products
    content.update({'products': serializeProducts(products), 'userAFIds': request.session['userAFIds'],
                    'sortForm': SortForm({'sortField': request.session['sortValue']})})

    return render(request, 'category.html', content)


def updateAFIdMap(request, selectValue, assistersData):
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


def resetAFIdMap(request, numAssisters):
    request.session['userAFIds'] = [[] for i in range(numAssisters)]


def updateSortValue(request, sortValue):
    request.session['sortValue'] = sortValue


def resetSortValue(request):
    request.session['sortValue'] = 'RANKING'


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
                                      'consSummary': product.consSummary, 'entryCapacity': product.entryCapacity,
                                      'cameraDescription': product.cameraDescription, 'batteryDescription': product.batteryDescription,
                                      'displayDescription': product.displayDescription},
                             'pros': Pro.objects.filter(product=product), 'cons': Con.objects.filter(product=product)})

    return productsData
