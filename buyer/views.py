from django.shortcuts import render
from .forms import SearchForm


def index(request):
    return render(request, 'index.html')


def product(request):
    form = SearchForm(request.GET)
    if not form.is_valid():
        return render(request, 'product.html')

    content = {'text': form.cleaned_data['text']}

    return render(request, 'product.html', content)


def about(request):
    return render(request, 'about.html')
