from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField()
    email = models.EmailField()
    password = models.TextField()
