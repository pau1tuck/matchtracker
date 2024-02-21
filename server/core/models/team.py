from django.db import models
from .stadium import Stadium
from .competition import Competition
from utils.constants import COUNTRIES, CONTINENTS, FEDERATIONS


class Team(models.Model):
    team_id = models.IntegerField()  # e.g. 45
    name = models.CharField(max_length=128)  # e.g. England
    country = models.CharField(max_length=64, choices=COUNTRIES)  # e.g. International
    continent = models.CharField(max_length=32, choices=CONTINENTS)  # e.g. Europe
    founded = models.IntegerField(null=True, blank=True)  # e.g. 1872
    federation = models.CharField(  # e.g. UEFA
        max_length=32, choices=FEDERATIONS, null=True, blank=True
    )
    stadium = models.ForeignKey(  # e.g. Wembley Stadium
        Stadium, on_delete=models.CASCADE, related_name="Stadium"
    )
    logo = models.ImageField(upload_to="teams/logos/")
    competitions = models.ManyToManyField(Competition, related_name="competitions")
    manager = models.CharField(max_length=128, null=True, blank=True)
    reputation = models.IntegerField(null=True, blank=True)
    primary_color = models.CharField(max_length=7, null=True, blank=True)  # HEX color
    secondary_color = models.CharField(max_length=7, null=True, blank=True)  # HEX color
    official_website = models.URLField(max_length=200, null=True, blank=True)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    twitter = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)


# Using both null=True and blank=True is common for non-string fields when you want to allow the field to be optional both at the form level (no validation error for empty values) and at the database level (storing an actual NULL value).
