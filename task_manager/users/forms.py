from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from .models import ExampleUser


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True, label=_('Имя'))
    last_name = forms.CharField(required=True, label=_('Фамилия'))

    class Meta(UserCreationForm.Meta):
        model = ExampleUser
        fields = ('first_name', 'last_name') + UserCreationForm.Meta.fields
