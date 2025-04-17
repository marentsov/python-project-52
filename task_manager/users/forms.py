from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserChangeForm,
    UserCreationForm,
)
from django.utils.translation import gettext as _
from task_manager.users.models import User


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


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "password1",
            "password2",
        )

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Enter your first name')})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Enter your last name')})
    )
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Enter your login')}))
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'placeholder': _('Enter your password')})
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password",
            'class': "form-control",
            'placeholder': _('Repeat your password')})
    )


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "password1",
            "password2",
        )

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Enter your first name')})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Enter your last name')})
    )
    username = forms.CharField(
        # required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Enter your login')}))
    password1 = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'placeholder': _('Enter your password')})
    )
    password2 = forms.CharField(
        # required=Fal
        required=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password",
            'class': "form-control",
            'placeholder': _('Repeat your password')})
    )