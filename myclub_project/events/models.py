from django.db import models


class MyclubUser(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField('Your Email')

    def __str__(self):
        return "Welcome, " + self.first_name + " " + self.last_name + "!"


class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=260)
    address = models.CharField(max_length=1000)
    zip_code = models.CharField('Zip Code', max_length=12)
    phone = models.CharField('Cell Phone', max_length=20)
    web = models.URLField('Web address')
    email_address = models.EmailField('Email address')

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.CharField(max_length=130)
    manager = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyclubUser)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
