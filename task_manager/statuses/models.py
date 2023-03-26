from django.db import models
from django.utils.translation import gettext as _


class Status(models.Model):
    """Model definition for Status."""
    name = models.CharField(max_length=130, unique=True)
    creatad_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Status."""
        verbose_name = _('Status')
        verbose_name_plural = _('Statuses')

    def __str__(self):
        """Unicode representation of Status."""
        return self.name
