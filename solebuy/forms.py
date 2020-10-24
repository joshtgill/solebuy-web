from django import forms


class CategoryForm(forms.Form):
    attributes = {'placeholder': 'Explore a category', 'autocomplete': 'off'}
    name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs=attributes))
