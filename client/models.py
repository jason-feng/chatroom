from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
    user = models.ForeignKey(User, null=True)
    # username field is useful to store guest name of unauthenticated users
    username = models.CharField(max_length=20)
    date = models.DateTimeField()
    content = models.CharField(max_length=5000)
