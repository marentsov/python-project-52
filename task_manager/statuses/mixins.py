from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _


class PreventUsedStatusDeletionMixin:
    # миксин предотвращающий удаление статусов которые назначены в задачах
    error_message = _('The status is in use and cannot be deleted')
    redirect_url = 'statuses:statuses'
    related_name = 'tasks'

    def post(self, request, *args, **kwargs):

        status = self.get_object()

        if getattr(status, self.related_name).exists():
            messages.error(request, self.error_message)
            return redirect(self.redirect_url)
        return super().post(request, *args, **kwargs)


# class StatusPermissionMixin(PermissionRequiredMixin):
#     permission_denied_message = _('The status is in use and cannot be deleted')
#     raise_exception = False
#
#     def handle_no_permission(self):
#         messages.error(self.request, self.permission_denied_message)
#         return redirect('statuses:statuses')