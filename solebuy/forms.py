from django import forms


class CategoryForm(forms.Form):
    name = forms.CharField(label='', max_length=20)
