from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext as _
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from users.forms import UserLoginForm, UserRegistrationForm, UserUpdateForm
from users.models import User


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    success_url = 'index'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task manager - authorization')
        return context

    def form_valid(self, form):
        message = _('You are logged in to your account')
        user = form.get_user()
        """Security check complete. Log the user in."""
        auth.login(self.request, user)
        messages.success(self.request, f"{user.username}, {message}")
        return HttpResponseRedirect(self.get_success_url())


class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = 'users/create.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    success_message = _('You have successfully registered!')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task manager - registration')
        return context

class UserUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'users/update.html'
    form_class = UserUpdateForm
    success_url = reverse_lazy('users:users')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        message = _('Личная информация обновлена')
        messages.success(self.request, message)
        return super().form_valid(form)

    def form_invalid(self, form):
        message = _('Ошибка обновления личной информации')
        messages.error(self.request, message)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task manager - update user info')
        return context

class UserListView(ListView):
    template_name = 'users/users.html'
    model = User
    queryset = User.objects.all().order_by('-id')
    context_object_name = 'users'


@login_required
def logout(request):
    message = _('Вы успешно вышли из аккаунта')
    messages.success(request, f"{request.user.username}, {message}")
    auth.logout(request)
    return redirect(reverse('index'))
# Create your views here.
