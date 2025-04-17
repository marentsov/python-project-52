from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from statuses.forms import StatusCreateForm, StatusUpdateForm
from statuses.mixins import PreventUsedStatusDeletionMixin
from statuses.models import Status


class StatusListView(LoginRequiredMixin, ListView):
    template_name = 'statuses/statuses.html'
    model = Status
    queryset = Status.objects.all().order_by('-id')
    context_object_name = 'statuses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task manager - statuses')
        return context


class StatusCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Status
    template_name = 'statuses/create.html'
    form_class = StatusCreateForm
    success_message = _('The status was created successfully')
    success_url = reverse_lazy('statuses:statuses')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task manager - create status')
        context['status'] = True
        return context

    # def form_valid(self, form):
    #     return super().form_valid(form)


class StatusUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Status
    template_name = 'statuses/update.html'
    form_class = StatusUpdateForm
    success_url = reverse_lazy('statuses:statuses')
    success_message = _('Status successfully updated')
    # queryset = Status.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task manager - update status info')
        # context['status'] = True
        return context


class StatusDeleteView(PreventUsedStatusDeletionMixin, SuccessMessageMixin, LoginRequiredMixin, DeleteView):

    model = Status
    success_url = reverse_lazy('statuses:statuses')
    template_name = 'statuses/delete.html'
    success_message = _('Status successfully deleted')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task manager - delete status')
        return context


# Create your views here.
