from django.shortcuts import render
from solebuy.forms import CategoryForm
from .forms import FilterForm, ProductForm
from buyer.src.assistant import Assistant
import json


def home(request):
    # Get all category names and associated icon path
    categoriesInfo = [(data.get('name'), data.get('iconPath')) for data in getCategoriesData()]

    # Build content for template
    content = {'categoryForm': CategoryForm(), 'categoriesInfo': categoriesInfo}

    return render(request, 'home.html', content)


def category(request):
    # Get the incoming category name
    categoryName = ''
    categoryForm = CategoryForm(request.GET)
    if categoryForm.is_valid():
        categoryName = categoryForm.cleaned_data['name']
    else:
        return render(request, 'category.html')

    # Attempt to get category data from name
    categoryData = getCategoryDataByName(categoryName)
    if not categoryData:
        content = {'categoryForm': categoryForm, 'filtersWidth': str(50), 'filterWidth': '100%'}
        return render(request, 'category.html', content)

    # Respond to the request
    product = None
    if request.method == 'POST':
        # Filter form submited. Update ID map with selection
        filterForm = FilterForm(request.POST)
        if filterForm.is_valid():
            updateIdMap(request, filterForm.cleaned_data)

        # Product form submitted. Get product data for popup
        productForm = ProductForm(request.POST)
        if productForm.is_valid():
            product = getProductDataByUrlName(categoryData.get('products'), productForm.cleaned_data['urlName'])
    else:
        product = None
        resetIdMap(request, len(categoryData.get('assisters')))

    # Find recommended products based on filter selections
    products = Assistant().findProducts(categoryData, request.session['idMap']).get('primary')
    products = sorted(products, key=lambda product: product.get('price'))

    # Build content for template
    content = {'categoryForm': categoryForm, 'data': categoryData,
               'assisters': categoryData.get('assisters'),
               'idMap': request.session['idMap'],
               'products': products,
               'product': product}

    return render(request, 'category.html', content)


def getCategoryDataByName(name):
    categoriesData = getCategoriesData()

    for data in categoriesData:
        if name == data.get('name'):
            return data

    return None


def getCategoriesData():
    with open('/home/joshtgill/Documents/proj/solebuy-web/local/categories.json', 'r') as filee:
        return json.load(filee)

    return {}


def updateIdMap(request, cleaned_data):
    selectValue = cleaned_data.get('button')
    assisterId = int(selectValue[ : selectValue.find('.')])
    filterId = int(selectValue[selectValue.find('.') + 1 : ])
    idMap = request.session['idMap']
    if filterId not in idMap[assisterId]:
        idMap[assisterId].append(filterId)
    else:
        idMap[assisterId].remove(filterId)

    request.session['idMap'] = idMap


def resetIdMap(request, numAssisters):
    request.session['idMap'] = [[] for i in range(numAssisters)]


def getProductDataByUrlName(products, urlName):
    for product in products:
        if product.get('urlName') == urlName:
            return product

    return None
