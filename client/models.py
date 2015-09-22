from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.

class Message(models.Model):
    username = models.CharField(max_length=20)
    date = models.DateTimeField()
    content = models.CharField(max_length=5000)

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['content']
