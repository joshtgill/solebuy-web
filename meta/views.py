from django.shortcuts import render
from solebuy.forms import CategoryForm


def about(request):
    return render(request, 'about.html', {'categoryForm': CategoryForm()})
