from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task manager - main')
        return context


# def index(request):
#     a = None
#     a.hello()  # Creating an error with an invalid line of code
#     return HttpResponse("Hello, world. You're at the pollapp index.")


# def index(request):
#     return render(
#         request,
#     'index.html',
#         context={
#             'title': 'главная Task-manager',
#             'hello': 'Привет от Task-manager',
#         }
#     )