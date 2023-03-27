from django.utils.translation import gettext as _
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView

from task_manager.tasks.models import Task
from task_manager.tasks.forms import TaskFrom, TaskFilterForm
from task_manager.core.permissions import IsOwner


class TaskListView(FilterView):
    filterset_class = TaskFilterForm
    tempalte_name = 'tasks/task_filter.html'


class TaskDetailView(DetailView):
    model = Task
    template_name = "tasks/task_detail.html"


class TaskCreateView(SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskFrom
    tempalte_name = 'tasks/task_form.html'
    success_url = '/tasks/'
    success_message = _('Задача успешно создана')

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.author = self.request.user
        self.obj.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(TaskCreateView, self).get_context_data(**kwargs)
        context['title'] = _('Создать задачу')
        context['btn_name'] = _('Создать')
        return context


class TaskUpdateView(SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskFrom
    tempalte_name = 'tasks/task_form.html'
    success_url = '/tasks/'
    success_message = _('Задача успешно изменена')

    def get_context_data(self, **kwargs):
        context = super(TaskUpdateView, self).get_context_data(**kwargs)
        context['title'] = _('Изменение задачи')
        context['btn_name'] = _('Изменить')
        return context


class TaskDeleteView(IsOwner, SuccessMessageMixin, DeleteView):
    model = Task
    tempalte_name = 'tasks/delete.html'
    success_url = '/tasks/'
    success_message = _('Задача успешно удалёна')
