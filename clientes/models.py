from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    documento = models.TextField(max_length=11)
    endereco = models.TextField(max_length=255)
    numero = models.TextField(max_length=10)
    cep = models.TextField(max_length=8)
