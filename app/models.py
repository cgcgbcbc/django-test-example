from django.db import models


# Create your models here.

class Activity(models.Model):
    remain_ticket = models.IntegerField()
