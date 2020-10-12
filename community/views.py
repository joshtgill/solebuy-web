from django.shortcuts import render
from solebuy.forms import SearchForm  # Probably shouldn't do this


def community(request):
    return render(request, 'community.html', {'searchForm': SearchForm()})
