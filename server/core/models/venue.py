from django.db import models


class Venue(models.Model):
    venue_id = models.IntegerField()  #  e.g, 8560
    name = models.CharField(max_length=128)  # e.g. Wembley Stadium
    city = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
