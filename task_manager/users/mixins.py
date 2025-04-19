from django.contrib import messages
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _


class UserPermissionMixin(LoginRequiredMixin, UserPassesTestMixin):

    permission_denied_message = _(
        "You don't have the rights to change another user."
    )
    login_message = _('You are not logged in! Please log in.')
    raise_exception = False
    index_url = reverse_lazy('users:users')
    login_url = reverse_lazy('login')

    def test_func(self):
        # проверка работы со своим профилем
        user = self.get_object()
        return user == self.request.user

    def handle_no_permission(self):
        # отказ в доступе
        if not self.request.user.is_authenticated:
            # пользователь не авторизован
            messages.info(self.request, self.login_message)
            return redirect(self.login_url)
        else:
            # пользователь авторизован, но не имеет прав
            messages.error(self.request, self.permission_denied_message)
            return redirect(self.index_url)


class PreventUsedUserDeletionMixin:
    # миксин предотвращающий удаление статусов которые назначены в задачах
    error_message = _('The user is in use and cannot be deleted')
    redirect_url = 'users:users'
    related_name = 'created_tasks'

    def post(self, request, *args, **kwargs):

        user = self.get_object()

        if getattr(user, self.related_name).exists():
            messages.error(request, self.error_message)
            return redirect(self.redirect_url)
        return super().post(request, *args, **kwargs)
