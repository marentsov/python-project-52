from django import forms
from django.utils.translation import gettext as _

from statuses.models import Status
from tasks.models import Task
from users.models import User


class TaskFilterForm(forms.Form):
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        required=False,
        label=_('Status'),
        widget=forms.Select(attrs={
            'class': 'form-control',}))

    executor = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=False,
        label=_('Executor'),
        widget=forms.Select(attrs={
            'class': 'form-control',}))

    my_tasks = forms.BooleanField(
        required=False,
        label=_('Only my tasks'),
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',}))


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'status', 'executor',)

    title = forms.CharField(
        widget=forms.TextInput(attrs={
            "autofocus": True,
            'class': 'form-control',
            'placeholder': _('Name')}))

    description = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Name')}))

    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        required=False,
        label=_('Status'),
        widget=forms.Select(attrs={
            'class': 'form-control', }))

    executor = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=False,
        label=_('Executor'),
        widget=forms.Select(attrs={
            'class': 'form-control', }))



class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'status', 'executor',)

    title = forms.CharField(
        widget=forms.TextInput(attrs={
            "autofocus": True,
            'class': 'form-control',
            'placeholder': _('Name')}))

    description = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Name')}))

    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        required=False,
        label=_('Status'),
        widget=forms.Select(attrs={
            'class': 'form-control', }))

    executor = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=False,
        label=_('Executor'),
        widget=forms.Select(attrs={
            'class': 'form-control', }))
