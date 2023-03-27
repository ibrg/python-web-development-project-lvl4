from django.db import models
from django.contrib.auth.models import AbstractUser


class ExampleUser(AbstractUser):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.get_full_name()

