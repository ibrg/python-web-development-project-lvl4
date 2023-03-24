
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils.translation import gettext as _


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
