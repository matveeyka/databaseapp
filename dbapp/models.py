from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    header = models.CharField(max_length=50)
    desc = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)