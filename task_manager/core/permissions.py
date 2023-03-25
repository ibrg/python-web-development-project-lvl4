from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _

from tasks.models import Task


class LoginRequired:
    login_url = '/login/'
    get_login_message = _('Вы не авторизованы! Пожалуйста, выполните вход.')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.get_login_message)
            return redirect(self.login_url)
        return super().dispatch(request, *args, **kwargs)


class AccessRequired:
    denied_message = _('У вас нет прав для изменения другого пользователя.')

    def has_permission(self):
        logged_user = self.get_object()
        user = self.request.user
        return user.id == logged_user.id

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            messages.error(request, self.denied_message)
            return redirect(request.META.get('HTTP_REFERER'))
        return super().dispatch(request, *args, **kwargs)


class CanDelete:
    error_message = _('Невозможно удалить статус, потому что он используется ')

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if Task.objects.filter(sattus=obj).count() > 0:
            messages.add_message(request, messages.ERROR, "Can't be deleted, has childern")
            return redirect('/')
        return super().delete(request, *args, **kwargs)


    
class IsOwner:
    alert_message = _('Задачу может удалить только её автор ')

    def has_object_permission(self, *args, **kwargs):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        obj = self.get_object()
        return obj.author == self.request.user

    def dispatch(self, request, *args, **kwargs):
        if not self.has_object_permission():
            messages.error(request, self.alert_message)
            return redirect(request.META.get('HTTP_REFERER'))
        return super().dispatch(request, *args, **kwargs)