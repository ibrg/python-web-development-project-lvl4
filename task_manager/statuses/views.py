from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import RestrictedError
from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from core.permissions import CanDelete, IsOwner

from .models import Status


class StatusListView(ListView):
    model = Status
    tempalte_name = 'statuses/list.html'


class StatusCreateView(SuccessMessageMixin, CreateView):
    model = Status
    fields = ['name']
    tempalte_name = 'statuses/status_form.html'
    success_url = '/statuses/'
    success_message = _('Статус успешно создан')

    def get_context_data(self, **kwargs):
        context = super(StatusCreateView, self).get_context_data(**kwargs)
        context['title'] = _('Создать статус')
        context['btn_name'] = _('Создать')
        return context


class StatusUpdateView(SuccessMessageMixin, UpdateView):
    model = Status
    fields = ['name']
    tempalte_name = 'statuses/status_form.html'
    success_url = '/statuses/'
    success_message = _('Статус успешно изменён')

    def get_context_data(self, **kwargs):
        context = super(StatusUpdateView, self).get_context_data(**kwargs)
        context['title'] = _('Изменение статуса ')
        context['btn_name'] = _('Изменить')
        return context


class StatusDeleteView(DeleteView):
    model = Status
    tempalte_name = 'statuses/delete.html'
    success_url = '/statuses/'
    success_message = _('Статус успешно удалён')
    error_message = _('Невозможно удалить статус, потому что он используется')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(request, self.success_message)
        except RestrictedError:
            messages.error(request, self.error_message)
        finally:
            return HttpResponseRedirect(success_url)
