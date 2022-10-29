from django import forms
from webapp.models import Products, Reviews


class ProductsListForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('name', 'category', 'description', 'image')


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=100,
        required=False,
        label='Search',
    )


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('review_text', 'rate')
