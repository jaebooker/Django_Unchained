from django.db import models

class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.CharField(max_length=130)
    manager = models.CharField(max_length=100)
    description = models.TextField(blank=True)
