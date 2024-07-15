from django.db import models
class signup(models.Model):
    firstname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    confirm_password=models.CharField(max_length=20)
# Create your models here.
