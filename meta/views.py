from django.shortcuts import render
from solebuy.forms import SearchForm


def about(request):
    return render(request, 'about.html', {'searchForm': SearchForm()})
