from django import forms
from django.contrib.auth.models import User
from webapp.models import Tasks, Statuses, Types, Projects
from webapp.widgets import DatePickerInput
from django.forms import widgets


class TasksListForm(forms.ModelForm):
    status = forms.ModelChoiceField(
        required=True,
        label='Status',
        queryset=Statuses.objects.all(),
        initial=[0]
    )
    type = forms.ModelMultipleChoiceField(
        required=True,
        label='Type',
        queryset=Types.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    project = forms.ModelChoiceField(
        required=False,
        label='Project',
        queryset=Projects.objects.all(),
    )

    class Meta:
        model = Tasks
        fields = ('summary', 'description', 'status', 'type', 'project')


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=100,
        required=False,
        label='Search',
    )


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ('summary', 'description', 'start_date', 'end_date')
        widgets = {
            'start_date': DatePickerInput(),
            'end_date': DatePickerInput(),
        }


class ProjectTasksForm(forms.ModelForm):
    status = forms.ModelChoiceField(
        required=True,
        label='Status',
        queryset=Statuses.objects.all(),
        initial=[0]
    )
    type = forms.ModelMultipleChoiceField(
        required=True,
        label='Type',
        queryset=Types.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Tasks
        fields = ('summary', 'description', 'status', 'type')


class ProjectUserAddForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['user']
        widgets = {
            'user': forms.CheckboxSelectMultiple
        }
