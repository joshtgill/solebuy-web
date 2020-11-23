from django.shortcuts import render
from solebuy.forms import CategoryForm
from buyer.models import Category


def home(request):
    # Get all category names
    content = {'categoryForm': CategoryForm(),
               'categoryNames': [category.name for category in Category.objects.all()]}

    return render(request, 'home.html', content)


def about(request):
    return render(request, 'about.html', {'categoryForm': CategoryForm()})
