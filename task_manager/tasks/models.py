from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings

from task_manager.statuses.models import Status
from task_manager.labels.models import Label


class Task(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Имя')
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    status = models.ForeignKey(Status, on_delete=models.RESTRICT, verbose_name="Статус")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author')
    executor = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='executors', 
        blank=True, 
        null=True, 
        verbose_name="Исполнитель"
        )
    labels = models.ManyToManyField(Label, related_name='labels', verbose_name="Метка", blank=True)
    creatad_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Task."""
        verbose_name = _('Задача')
        verbose_name_plural = _('Задачи')

    def __str__(self):
        """Unicode representation of Task."""
        return self.name
