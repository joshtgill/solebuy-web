from django import forms


class SearchForm(forms.Form):

    attributes = {'placeholder': 'Explore a category', 'autocomplete': 'off'}
    search = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs=attributes))
