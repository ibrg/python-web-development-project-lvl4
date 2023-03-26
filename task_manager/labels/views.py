from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from tasks.models import Task
from .models import Label


class LabelListView(ListView):
    model = Label
    tempalte_name = 'labels/list.html'


class LabelCreateView(SuccessMessageMixin, CreateView):
    model = Label
    fields = ['name']
    tempalte_name = 'labels/label_form.html'
    success_url = '/labels/'
    success_message = _('Метка успешно создана')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Создать метку')
        context['btn_name'] = _('Создать')
        return context


class LabelUpdateView(SuccessMessageMixin, UpdateView):
    model = Label
    fields = ['name']
    tempalte_name = 'labels/label_form.html'
    success_url = '/labels/'
    success_message = _('Метка успешно изменена')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Изменение метки')
        context['btn_name'] = _('Изменить')
        return context


class LabelDeleteView(DeleteView):
    model = Label
    tempalte_name = 'labels/label_confirm_delete'
    success_url = '/labels/'
    success_message = _('Метка успешно удалена')
    error_message = _('Невозможно удалить метку, потому что она используется')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            if Task.objects.filter(labels=self.object).exists():
                messages.error(request, self.error_message)
                return
            self.object.delete()
            messages.success(request, self.success_message)
        finally:
            return HttpResponseRedirect(success_url)
