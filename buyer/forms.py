from django import forms


class FilterForm(forms.Form):
    button = forms.CharField()


class ProductForm(forms.Form):
    name = forms.CharField()
