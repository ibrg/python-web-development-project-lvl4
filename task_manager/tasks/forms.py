import django_filters
from django import forms
from django.utils.translation import gettext as _
from task_manager.labels.models import Label
from .models import Task


class TaskFrom(forms.ModelForm):

    class Meta:
        model = Task
        exclude = ('author', 'created_at')


class TaskFilterForm(django_filters.FilterSet):

    self_tasks = django_filters.BooleanFilter(
        widget=forms.CheckboxInput,
        method='get_self_tasks',
        label=_('Только свои задачи'))

    labels = django_filters.ModelChoiceFilter(
        field_name='labels',
        label='Метка',
        queryset=Label.objects.all())

    def get_self_tasks(self, queryset, name, value):
        if value:
            queryset = queryset.filter(author=self.request.user)
        return queryset

    class Meta:
        model = Task
        fields = ('status', 'labels', 'executor', 'self_tasks')
