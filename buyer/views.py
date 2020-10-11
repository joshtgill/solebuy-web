from django.shortcuts import render
from .forms import SearchForm, SelectForm
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
        return render(request, 'product.html', {'searchForm': searchForm, 'filterWidth': '100%'})

    # Initialize select form(s)
    selectForms = []
    for assister in category.get('assisters'):
        # Get select form info from data
        title = assister.get('label')
        prompt = assister.get('prompt')
        choices = [(i, assister.get('filters')[i]) for i in range(len(assister.get('filters')))]

        # Build select form
        selectForm = SelectForm(title=title, prompt=prompt, choices=choices, initiall=None)
        if request.method == 'POST':
            selectForm = SelectForm(request.POST, title=title, prompt=prompt, choices=choices, initiall=None)
            if selectForm.is_valid():
                selectForm.initiall = selectForm.cleaned_data.get(selectForm.title)

        selectForms.append(selectForm)

    content = {'searchForm': searchForm, 'category': category, 'selectForms': selectForms, 'filterWidth': str(len(selectForms))}
    return render(request, 'product.html', content)


def about(request):
    return render(request, 'about.html')
