from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class information(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)