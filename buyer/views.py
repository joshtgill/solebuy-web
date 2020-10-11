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
    search = form.cleaned_data['search']

    # Lookup the category from search
    categoriesData = {}
    with open('/home/joshtgill/Documents/proj/solebuy-web/local/categories.json', 'r') as filee:
        categoriesData = json.load(filee)
    category = {}
    for categoryData in categoriesData:
        if search == categoryData.get('name'):
            category = categoryData

    # Initialize search form
    searchForm = SearchForm(initial={'search': category.get('name')})

    # Searched category not found
    if not category:
        return render(request, 'product.html', {'searchForm': searchForm, 'filtersWidth': str(50), 'filterWidth': '100%'})

    # Find the recommended product(s)
    idMap = []
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            selectValue = form.cleaned_data.get('filterButton')
            assisterId = int(selectValue[ : selectValue.find('.')])
            filterId = int(selectValue[selectValue.find('.') + 1 : ])
            idMap = request.session['idMap']
            if filterId not in idMap[assisterId]:
                idMap[assisterId].append(filterId)
            else:
                idMap[assisterId].remove(filterId)

            request.session['idMap'] = idMap
    else:
        # Reset id map on GET request (aka search)
        request.session['idMap'] = [[] for i in range(len(category.get('assisters')))]

    content = {'searchForm': searchForm, 'category': category, 'filtersWidth': str(30 + len(category.get('assisters')) * 10), 'filterWidth': str(len(category.get('assisters'))), 'results': Assistant().findProducts(category, idMap)}
    return render(request, 'product.html', content)


def about(request):
    return render(request, 'about.html')
