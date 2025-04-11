from django.shortcuts import render

from django.views.generic import TemplateView
from django.utils.translation import gettext as _


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task manager - main')
        return context


# def index(request):
#     return render(
#         request,
#     'index.html',
#         context={
#             'title': 'главная Task-manager',
#             'hello': 'Привет от Task-manager',
#         }
#     )