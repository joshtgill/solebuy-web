from django.shortcuts import render
from solebuy.forms import CategoryForm
from .forms import FilterForm
from buyer.src.assistant import Assistant
import json


def home(request):
    # Get all category names and associated icon path
    categoriesInfo = [(data.get('name'), data.get('iconPath')) for data in getCategoriesData()]

    # Build content for template
    content = {'categoryForm': CategoryForm(), 'categoriesInfo': categoriesInfo}

    return render(request, 'home.html', content)


def category(request):
    # Attempt to get category name
    name = ''
    form = CategoryForm(request.GET)
    if form.is_valid():
        name = form.cleaned_data['name']
    else:
        return render(request, 'category.html')

    # Attempt to get category data
    data = getCategoryDataByName(name)
    if not data:
        content = {'categoryForm': form, 'filtersWidth': str(50), 'filterWidth': '100%'}
        return render(request, 'category.html', content)

    # Find the recommended product(s)
    updateIdMap(request) if request.method == 'POST' else resetIdMap(request, len(data.get('assisters')))
    products = Assistant().findProducts(data, request.session['idMap']).get('primary')
    products = sorted(products, key=lambda product: product.get('price'))

    # Build content for template
    content = {'categoryForm': form, 'data': data,
               'assisters': data.get('assisters'),
               'idMap': request.session['idMap'],
               'products': products}

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
