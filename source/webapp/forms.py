from django import forms
from django.contrib.auth.models import User
from webapp.models import Products, Reviews
from webapp.widgets import DatePickerInput
from django.forms import widgets


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

#
#
# class ProjectTasksForm(forms.ModelForm):
#     status = forms.ModelChoiceField(
#         required=True,
#         label='Status',
#         queryset=Statuses.objects.all(),
#         initial=[0]
#     )
#     type = forms.ModelMultipleChoiceField(
#         required=True,
#         label='Type',
#         queryset=Types.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#     )
#
#     class Meta:
#         model = Tasks
#         fields = ('summary', 'description', 'status', 'type')
#
#
# class ProjectUserAddForm(forms.ModelForm):
#     class Meta:
#         model = Projects
#         fields = ['user']
#         widgets = {
#             'user': forms.CheckboxSelectMultiple
#         }
