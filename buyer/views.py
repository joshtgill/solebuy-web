from django.shortcuts import render
from .forms import SearchForm
import json


def index(request):
    return render(request, 'index.html')


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

    content = {'category': category, 'filterWidth': str(len(category.get('assisters')))}

    return render(request, 'product.html', content)


def about(request):
    return render(request, 'about.html')
