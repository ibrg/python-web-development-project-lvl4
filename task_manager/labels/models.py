from django.db import models
from django.utils.translation import gettext as _


class Label(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Status."""
        verbose_name = _('Меткa')
        verbose_name_plural = _('Метки')

    def __str__(self):
        return self.name
