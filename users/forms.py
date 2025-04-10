from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext as _

from users.models import User


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "autofocus": True,
            'class': 'form-control',
            'placeholder': _('Enter your login')}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password",
            'class': "form-control",
            'placeholder': _('Enter your password')}))

    class Meta:
        model = User
        fields = ['username', 'password']