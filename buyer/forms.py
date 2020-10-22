from django import forms


class FilterForm(forms.Form):
    button = forms.CharField()
