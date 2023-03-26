from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _

from statuses.models import Status
from labels.models import Label


class Task(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.RESTRICT)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    executor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='executor', blank=True, null=True)
    labels = models.ManyToManyField(Label, related_name='labels')
    creatad_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Task."""
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')

    def __str__(self):
        """Unicode representation of Task."""
        return self.name
