from django.db import models


class Stadium(models.Model):
    stadium_id = models.IntegerField(primary_key=True)  #  e.g, 8560
    name = models.CharField(max_length=128)  # e.g. Wembley Stadium
    city = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    capacity = models.IntegerField
