from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.translation import gettext as _
from django.shortcuts import render, redirect

from users.forms import UserLoginForm

class UserLoginView(LoginView):
    template_name = 'login.html'
    form_class = UserLoginForm
    success_url = 'main:index'

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



@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Вы успешно вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:index'))
# Create your views here.
