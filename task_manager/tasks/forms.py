import django_filters
from django import forms

from task_manager.labels.models import Label
from .models import Task


class TaskFrom(forms.ModelForm):
    status = forms.CharField(required=True, label='Статус')
    executor = forms.CharField(required=True, label='Исполнитель')

    class Meta:
        model = Task
        # fields = ['status',]
        exclude = ('author', 'created_at')


class TaskFilterForm(django_filters.FilterSet):

    self_tasks = django_filters.BooleanFilter(
        widget=forms.CheckboxInput,
        method='get_self_tasks',
        label='Только свои задачи')

    labels = django_filters.ModelChoiceFilter(
        field_name='labels',
        label='Метка',
        queryset=Label.objects.all()
    )
  
    def get_self_tasks(self, queryset, name, value):
        if value:
            queryset = queryset.filter(author=self.request.user)
        return queryset

    class Meta:
        model = Task
        fields = ('status', 'labels',  'executor', 'self_tasks')
