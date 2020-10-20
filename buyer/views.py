from django.shortcuts import render
from solebuy.forms import SearchForm
from .forms import FilterForm, ProductForm
from buyer.src.assistant import Assistant
import json


def home(request):
    # Get category names and icon path
    categoriesData = getCategoriesData()
    categoriesInfo = [(categoryData.get('name'), categoryData.get('iconPath')) for categoryData in categoriesData]

    # Build content for template
    content = {'searchForm': SearchForm(), 'categoriesInfo': categoriesInfo}

    return render(request, 'home.html', content)


def category(request):
    # Get the search
    form = SearchForm(request.GET)
    if not form.is_valid():
        return render(request, 'category.html')

    # Get category data from search text
    categoryData = getCategoryData(form.cleaned_data['name'])
    if not categoryData:
        content = {'searchForm': form, 'filtersWidth': str(50), 'filterWidth': '100%'}
        return render(request, 'category.html', content)

    # Find the recommended product(s)
    updateIdMap(request) if request.method == 'POST' else resetIdMap(request, len(categoryData.get('assisters')))
    products = Assistant().findProducts(categoryData, request.session['idMap']).get('primary')
    products = sorted(products, key=lambda product: product.get('price'))

    # Build content for template
    content = {'searchForm': form, 'categoryData': categoryData,
               'assisters': categoryData.get('assisters'),
               'idMap': request.session['idMap'],
               'products': products}

    return render(request, 'category.html', content)


def getCategoryData(searchText):
    categoriesData = getCategoriesData()

    for categoryData in categoriesData:
        if searchText == categoryData.get('name'):
            return categoryData

    return None


def getCategoriesData():
    with open('/home/joshtgill/Documents/proj/solebuy-web/local/categories.json', 'r') as filee:
        return json.load(filee)

    return {}


def updateIdMap(request):
    form = FilterForm(request.POST)
    if form.is_valid():
        selectValue = form.cleaned_data.get('button')
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


def product(request):
    form = ProductForm(request.GET)
    if form.is_valid():
        urlName = form.cleaned_data.get('name')
        return render(request, 'product.html', {'searchForm': SearchForm(), 'product': getProductByUrlName(urlName)})

    return render(request, 'product.html', {'searchForm': SearchForm()})


def getProductByUrlName(urlName):
    for product in getCategoriesData()[0].get('products'):
        if product.get('urlName') == urlName:
            return product

    return None
