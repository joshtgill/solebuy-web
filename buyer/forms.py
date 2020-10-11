from django import forms


class SearchForm(forms.Form):
    attributes = {'placeholder': 'Explore a category', 'autocomplete': 'off'}
    search = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs=attributes))


class SelectForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.title = kwargs.pop('title')
        self.prompt = kwargs.pop('prompt')
        self.choices = kwargs.pop('choices')
        self.initiall = kwargs.pop('initiall')
        super(SelectForm, self).__init__(*args, **kwargs)

        self.fields[self.title] = forms.ChoiceField(label='', choices=self.choices)
        self.fields[self.title].initial = self.initiall
