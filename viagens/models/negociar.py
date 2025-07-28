from django.db import models
from django.contrib.auth import get_user_model

user_model = get_user_model()

class Negociar(models.Model):
    whatsApp = models.CharField(max_length=11, null=True)
    instagram = models.TextField(null=True)
    facebook = models.TextField(null=True)
    email = models.TimeField(null=True)
    def __str__(self):
        return self.whatsApp 