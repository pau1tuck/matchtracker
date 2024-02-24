from django.db import models
from utils.constants import COUNTRIES
from utils.constants import COMPETITION_TYPES


class Competition(models.Model):
    competition_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)  # e.g. League One
    country = models.CharField(max_length=64, choices=COUNTRIES)  # e.g. England
    competition_type = models.CharField(  # e.g. LEAGUE
        max_length=64, choices=COMPETITION_TYPES
    )  # e.g. England
    sponsor = models.CharField(max_length=64, null=True, blank=True)
