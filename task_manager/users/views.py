from django.contrib import auth, messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from task_manager.users.forms import UserLoginForm, UserRegistrationForm, UserUpdateForm
from task_manager.users.mixins import UserPermissionMixin, PreventUsedUserDeletionMixin
from task_manager.users.models import User


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
        messages.success(self.request, f"{message}")
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


class UserUpdateView(UserPermissionMixin, UpdateView):
    model = User
    template_name = 'users/update.html'
    form_class = UserUpdateForm
    success_url = reverse_lazy('users:users')

    # УДАЛЕНО переопределение get_object - теперь используем стандартное получение объекта

    def form_valid(self, form):
        messages.success(self.request, _('User info was updated'))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('User info update error.'))
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task manager - update user info')
        return context


class UserDeleteView(PreventUsedUserDeletionMixin, UserPermissionMixin, DeleteView):
    model = User
    success_url = reverse_lazy('users:users')
    template_name = 'users/delete.html'
    success_message = _('User successfully deleted')

    def delete(self, request, *args, **kwargs):
        messages.success(request, self.success_message)
        return super().delete(request, *args, **kwargs)


# class UserUpdateView(UserPermissionMixin, UpdateView):
#     model = User
#
#     template_name = 'users/update.html'
#     form_class = UserUpdateForm
#     success_url = reverse_lazy('users:users')
#
#
#     def get_object(self, queryset=None):
#         return self.request.user
#
#     def form_valid(self, form):
#         message = _('User info was updated')
#         messages.success(self.request, message)
#         return super().form_valid(form)
#
#     def form_invalid(self, form):
#         message = _('User info update error.')
#         messages.error(self.request, message)
#         return super().form_invalid(form)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = _('Task manager - update user info')
#         return context
#
#
# class UserDeleteView(UserPermissionMixin, SuccessMessageMixin, DeleteView):
#
#     model = User
#     success_url = reverse_lazy('index')
#     template_name = 'users/delete.html'
#     success_message = _('User successfully deleted')
#
#
class UserListView(ListView):
    template_name = 'users/users.html'
    model = User
    queryset = User.objects.all().order_by('-id')
    context_object_name = 'users'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task manager - users')
        return context


class UserLogoutView(LoginView):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            messages.info(request, _('You are logged out'))
        return redirect('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task manager - logout')
        return context



# @login_required
# def logout(request):
#     message = _('You have successfully logged out of your account')
#     messages.success(request, f"{request.user.username}, {message}")
#     auth.logout(request)
#     return redirect(reverse('index'))
# # Create your views here.
