from django.db import models
from .stadium import Stadium
from .competition import Competition
from utils.constants import COUNTRIES

CONTINENTS = [
    ("Africa", "Africa"),
    ("Asia", "Asia"),
    ("Europe", "Europe"),
    ("North America", "North America"),
    ("Oceania", "Oceania"),
    ("South America", "South America"),
]

FEDERATIONS = []


class Team(models.Model):
    name = models.CharField(max_length=128)
    country = models.CharField(max_length=64, choices=COUNTRIES)  # e.g. England
    continent = models.CharField(max_length=32, choices=CONTINENTS)
    logo = models.ImageField(upload_to="teams/logos/")
    stadium = models.ForeignKey(
        Stadium, on_delete=models.CASCADE, related_name="Stadium"
    )
    competitions = models.ManyToManyField(Competition, related_name="competitions")
    founded = models.IntegerField(null=True, blank=True)
    manager = models.CharField(max_length=128, null=True, blank=True)
    reputation = models.IntegerField(null=True, blank=True)
    primary_color = models.CharField(max_length=7, null=True, blank=True)  # HEX color
    secondary_color = models.CharField(max_length=7, null=True, blank=True)  # HEX color
    official_website = models.URLField(max_length=200, null=True, blank=True)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    twitter = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)


# Using both null=True and blank=True is common for non-string fields when you want to allow the field to be optional both at the form level (no validation error for empty values) and at the database level (storing an actual NULL value).
