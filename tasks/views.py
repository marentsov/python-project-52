from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _

from tasks.forms import TaskFilterForm, TaskCreateForm, TaskUpdateForm
from tasks.models import Task


class TaskListView(LoginRequiredMixin, ListView):

    template_name = 'tasks/tasks.html'
    model = Task
    context_object_name = 'tasks'

    def get_queryset(self):

        status = self.request.GET.get('status')
        executor = self.request.GET.get('executor')
        label = self.request.GET.get('label')
        my_tasks = self.request.GET.get('my_tasks')

        tasks = Task.objects.all().order_by('-id') # базовый queryset

        if status: # если выбран статус
            tasks = tasks.filter(status_id=status)
        if executor: # если выбран исполнитель
            tasks = tasks.filter(executor_id=executor)
        if label:
            tasks = tasks.filter(label_id=labels)
        if my_tasks == 'on': # если выбрана опция "только мои задачи"
            tasks = tasks.filter(creator=self.request.user)

        return tasks

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = TaskFilterForm(self.request.GET)
        context['title'] = _('Task manager - tasks')
        return context

class TaskCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):

    model = Task
    template_name = 'tasks/create.html'
    form_class = TaskCreateForm
    success_message = _('The task was created successfully')
    success_url = reverse_lazy('tasks:tasks')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task manager - create task')
        context['task'] = True
        return context


    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class TaskUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):

    model = Task
    template_name = 'tasks/update.html'
    form_class = TaskUpdateForm
    success_message = _('The task was updated successfully')
    success_url = reverse_lazy('tasks:tasks')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task manager - update task')
        context['task'] = True
        return context


class TaskDetailView(LoginRequiredMixin, DetailView):

    model = Task
    template_name = 'tasks/task.html'
    context_object_name = "task"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task manager - detail view of task')
        return context


class TaskDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):

    model = Task
    success_url = reverse_lazy('tasks:tasks')
    template_name = 'tasks/delete.html'
    success_message = _('Task successfully deleted')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task manager - delete task')
        return context











# Create your views here.
