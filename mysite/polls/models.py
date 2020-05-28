from django.db import models

# Create your models here.
class NotAPoll(models.Model):
    text = models.IntegerField()
