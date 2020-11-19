from django import forms


class FilterForm(forms.Form):
    filterField = forms.CharField()


class SortForm(forms.Form):
    sortField = forms.ChoiceField(label='Sort by',
                                  widget=forms.Select(attrs={'onchange': 'this.form.submit();'}),
                                  choices = (('RANKING', 'Our ranking (best to worst)'),
                                             ('PRICE_LOW', 'Starting price (low to high)'),
                                             ('PRICE_HIGH', 'Starting price (high to low)')))
