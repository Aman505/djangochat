from django.db import models
from datetime import datetime

class Room(models.Model):
    name = models.CharField(max_length=10000)
class Messages(models.Model):
    value=models.CharField(max_length=1000000)
    datetime=models.DateTimeField(default=datetime.now, blank=True)
    user=models.CharField(max_length=1000000)
    room=models.CharField(max_length=1000000)



