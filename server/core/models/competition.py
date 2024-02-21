from django.db import models
from Utils.constants import COUNTRY_CHOICES

COMPETITION_TYPES = [
    ("League", "League"),
    ("Cup", "Cup"),
    ("International", "International"),
    ('Friendly, "Friendly'),
    ("Charity", "Charity"),
    ("Exhibition", "Exhibition"),
]


class Competition(models.Model):
    competition_id = models.IntegerField()
    name = models.CharField(max_length=128)  # e.g. League One
    country = models.CharField(max_length=64, choices=COUNTRY_CHOICES)  # e.g. England
    season = models.CharField(max_length=16)  # e.g. 2023/24
    stage = models.CharField(
        max_length=64, blank=True
    )  # e.g. Group Stage, Quarter-Finals
    logo = models.ImageField(upload_to="media/competitions/")
    flag = models.ImageField(upload_to="media/flags/")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
