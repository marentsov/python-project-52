from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _



class PreventUsedLabelsDeletionMixin:
    # миксин предотвращающий удаление статусов которые назначены в задачах
    error_message = _('The label is in use and cannot be deleted')
    redirect_url = 'labels:labels'
    related_name = 'tasks_label'

    def post(self, request, *args, **kwargs):

        label = self.get_object()

        if getattr(label, self.related_name).exists():
            messages.error(request, self.error_message)
            return redirect(self.redirect_url)
        return super().post(request, *args, **kwargs)