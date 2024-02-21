from django.db import models
from utils.constants import COUNTRIES
from utils.constants import COMPETITION_TYPES


class Competition(models.Model):
    competition_id = models.IntegerField()
    name = models.CharField(max_length=128)  # e.g. League One
    country = models.CharField(max_length=64, choices=COUNTRIES)  # e.g. England
    competition_type = models.CharField(
        max_length=64, choices=COMPETITION_TYPES
    )  # e.g. England
    #!   association = ?
    season = models.CharField(max_length=16)  # e.g. 2023/24
    stage = models.CharField(
        max_length=64, blank=True
    )  # e.g. Group Stage, Quarter-Finals
    logo = models.ImageField(upload_to="media/competitions/")
    flag = models.ImageField(upload_to="media/flags/")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
