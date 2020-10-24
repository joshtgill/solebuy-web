from django.shortcuts import render
from solebuy.forms import CategoryForm  # Probably shouldn't do this


def community(request):
    return render(request, 'community.html', {'categoryForm': CategoryForm()})
