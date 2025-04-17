from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from task_manager.labels.forms import LabelCreateForm, LabelUpdateForm
from task_manager.labels.mixins import PreventUsedLabelsDeletionMixin
from task_manager.labels.models import Label


class LabelListView(LoginRequiredMixin, ListView):
    template_name = 'labels/labels.html'
    model = Label
    queryset = Label.objects.all().order_by('-id')
    context_object_name = 'labels'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task manager - labels')
        return context


class LabelCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Label
    template_name = 'labels/create.html'
    form_class = LabelCreateForm
    success_message = _('The label was created successfully')
    success_url = reverse_lazy('labels:labels')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task manager - create label')
        context['label'] = True
        return context


class LabelUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Label
    template_name = 'labels/update.html'
    form_class = LabelUpdateForm
    success_url = reverse_lazy('labels:labels')
    success_message = _('Label successfully updated')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task manager - update label info')
        # context['status'] = True
        return context


class LabelDeleteView(PreventUsedLabelsDeletionMixin, SuccessMessageMixin, LoginRequiredMixin, DeleteView):

    model = Label
    success_url = reverse_lazy('labels:labels')
    template_name = 'labels/delete.html'
    success_message = _('Label successfully deleted')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task manager - delete label')
        return context