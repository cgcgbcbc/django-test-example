from django.db import models


# Create your models here.

class Activity(models.Model):
    remain_ticket = models.IntegerField()


class Ticket(models.Model):
    activity = models.ForeignKey(Activity)
    user = models.CharField(max_length=64, db_index=True)
