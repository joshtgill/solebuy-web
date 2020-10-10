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

    # Lookup the cateogry
    categoriesData = {}
    with open('/home/joshtgill/Documents/proj/solebuy-web/local/categories.json', 'r') as filee:
        categoriesData = json.load(filee)
    category = {}
    for categoryData in categoriesData:
        if search == categoryData.get('name'):
            category = categoryData
    if not category:
        return render(request, 'product.html', {'filterWidth': '100%'})

    # Initialize search form
    searchForm = SearchForm(initial={'search': category.get('name')})

    # Initialize select form(s)
    selectForms = []
    for assister in category.get('assisters'):
        choices = []
        for filterr in assister.get('filters'):
            choices.append((filterr, filterr))

        selectForms.append(SelectForm(title=assister.get('label'), choices=tuple(choices)))

    # If request is POST, get value from select form(s)
    if request.method == 'POST':
        for form in selectForms:
            postForm = SelectForm(request.POST, title=form.title, choices=form.choices)
            if postForm.is_valid():
                print(postForm.cleaned_data.get(form.title))

    content = {'searchForm': searchForm, 'category': category, 'selectForms': selectForms, 'filterWidth': str(len(selectForms))}
    return render(request, 'product.html', content)


def about(request):
    return render(request, 'about.html')
