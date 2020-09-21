from django.db import models

app_name = 'messageapp'

class MessagesModel(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    message = models.TextField(max_length=250)
