from django.db import models
from django.contrib.auth import get_user_model

user_model = get_user_model()

class Agencia(models.Model):
    name = models.CharField(max_length=105)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    user = models.ForeignKey(user_model, on_delete=models.PROTECT)

    def __str__(self):
        return self.name