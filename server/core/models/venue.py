from django.db import models


class Venue(models.Model):
    venue_id = models.IntegerField()
    name = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    country = models.CharField(max_length=128)