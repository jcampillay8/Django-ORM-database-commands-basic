from django.db import models

# Create your models here.
class Users(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email_address = models.EmailField()
    age = models.CharField(max_length=3)
