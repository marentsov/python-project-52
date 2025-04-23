from django.contrib import messages
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _


class UserTaskPermissionMixin(LoginRequiredMixin, UserPassesTestMixin):
    # миксин который запрещает удаление задачи не ее автором
    permission_denied_message = _("Task can only be deleted by author.")
    raise_exception = False
    index_url = reverse_lazy('tasks:tasks')

    def test_func(self):
        # проверка работы со своей задачей
        task_creator = self.get_object().creator
        return task_creator == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return redirect(self.index_url)