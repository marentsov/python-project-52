from django.shortcuts import render

from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'главная Task manager'
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