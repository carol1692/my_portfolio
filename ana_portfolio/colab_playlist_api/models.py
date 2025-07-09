from django.db import models

class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    
