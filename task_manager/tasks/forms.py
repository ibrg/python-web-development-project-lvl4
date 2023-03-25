from django import forms

from .models import Task


class TaskFrom(forms.ModelForm):

    class Meta:
        model = Task
        exclude = ('author', 'created_at')
