from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from core.permissions import AccessRequired, LoginRequired

from .forms import UserRegistrationForm


class Login(SuccessMessageMixin, LoginView):
    template_name = 'registration/login.html'
    success_message = _('Вы залогинены')

    def get_context_data(self, **kwargs):
        context = super(Login, self).get_context_data(**kwargs)
        context['btn_name'] = _('Войти')
        return context


class Logout(SuccessMessageMixin, LogoutView):
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, _('Вы разлогинены'))
        return response


class UserListView(ListView):
    model = User
    template_name = "registration/user_list.html"


class UserUpdateView(LoginRequired, AccessRequired, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "registration/user_update.html"
    template_name_suffix = '_update_form'
    success_url = '/users/'
    success_message = _('Пользователь успешно изменён')

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['btn_name'] = _('Изменить')
        return context


class UserCreateView(SuccessMessageMixin, CreateView):
    # cratate user == registration user
    form_class = UserRegistrationForm
    template_name = 'registration/user_create.html'
    success_message = 'Пользователь успешно зарегистрирован'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['btn_name'] = _('Зарегистрировать')
        return context


class UserDelete(LoginRequired, AccessRequired, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'registration/user_delete.html'
    success_url = reverse_lazy('users_list')
    success_message = _('Пользователь успешно удалён')
