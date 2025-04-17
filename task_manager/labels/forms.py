from django import forms
from django.utils.translation import gettext as _
from task_manager.labels.models import Label


class LabelCreateForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ('name',)

    name = forms.CharField(
        widget=forms.TextInput(attrs={
            "autofocus": True,
            'class': 'form-control',
            'placeholder': _('Name')}))


class LabelUpdateForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ('name',)

    name = forms.CharField(
        widget=forms.TextInput(attrs={
            "autofocus": True,
            'class': 'form-control',
            'placeholder': _('Name')}))