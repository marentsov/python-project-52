from django import forms
from django.utils.translation import gettext as _

from statuses.models import Status


class StatusCreateForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ('name',)

    name = forms.CharField(
        widget=forms.TextInput(attrs={
            "autofocus": True,
            'class': 'form-control',
            'placeholder': _('Name')}))


class StatusUpdateForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ('name',)

    name = forms.CharField(
        widget=forms.TextInput(attrs={
            "autofocus": True,
            'class': 'form-control',
            'placeholder': _('Name')}))