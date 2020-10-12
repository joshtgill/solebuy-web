from django.shortcuts import render
from .forms import SearchForm, FilterForm
from buyer.src.assistant import Assistant
import json


def index(request):
    return render(request, 'index.html', {'searchForm': SearchForm()})


def product(request):
    # Get the search
    form = SearchForm(request.GET)
    if not form.is_valid():
        return render(request, 'product.html')

    # Get category data from search text
    categoryData = getCategoryData(form.cleaned_data['text'])
    if not categoryData:
        content = {'searchForm': form, 'filtersWidth': str(50), 'filterWidth': '100%'}
        return render(request, 'product.html', content)

    # Find the recommended product(s)
    updateIdMap(request) if request.method == 'POST' else resetIdMap(request, len(categoryData.get('assisters')))
    results = Assistant().findProducts(categoryData, request.session['idMap'])

    # Build content for template
    content = {'searchForm': form, 'categoryData': categoryData,
               'assisters': categoryData.get('assisters'),
               'idMap': request.session['idMap'],
               'results': results}

    return render(request, 'product.html', content)


def getCategoryData(searchText):
    categoriesData = {}
    with open('/home/joshtgill/Documents/proj/solebuy-web/local/categories.json', 'r') as filee:
        categoriesData = json.load(filee)

    for categoryData in categoriesData:
        if searchText == categoryData.get('name'):
            return categoryData

    return None


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


def about(request):
    return render(request, 'about.html')
