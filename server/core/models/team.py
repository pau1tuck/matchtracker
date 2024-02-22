from django.db import models
from .stadium import Stadium
from .competition import Competition
from utils.constants import COUNTRIES, CONTINENTS, FEDERATIONS


class Team(models.Model):
    team_id = models.IntegerField(primary_key=True)  # e.g. 45
    name = models.CharField(max_length=128)  # e.g. Manchester United
    short_name = models.CharField(max_length=128, null=True, blank=True)  # e.g. Man Utd
    abbreviation = models.CharField(max_length=3)  # MNU
    country = models.CharField(max_length=64, choices=COUNTRIES)  # e.g. England
    continent = models.CharField(max_length=32, choices=CONTINENTS)  # e.g. Europe
    founded = models.IntegerField(null=True, blank=True)  # e.g. 1872
    federation = models.CharField(  # e.g. UEFA
        max_length=32, choices=FEDERATIONS, null=True, blank=True
    )
    stadium = models.ForeignKey(  # e.g. Old Trafford
        Stadium, on_delete=models.CASCADE, related_name="stadium"
    )
    logo = models.ImageField(upload_to="teams/logos/")
    # ? icon = models.ImageField(upload_to="teams/icons/")  # Two-toned strips alongside the score on TNT. Use CSS and primary, secondary, (tertiary) colors to create a vertical rectangle with two colors.
    manager = models.CharField(
        max_length=128, null=True, blank=True
    )  # e.g. Erik Ten Hag
    owner = models.CharField(max_length=128, null=True, blank=True)  # e.g.
    sponsor = models.CharField(max_length=128, null=True, blank=True)
    competitions = models.ManyToManyField(Competition, related_name="competitions")
    world_ranking = models.IntegerField(null=True, blank=True)
    primary_color = models.CharField(max_length=16, null=True, blank=True)  # HEX color
    secondary_color = models.CharField(
        max_length=16, null=True, blank=True
    )  # HEX color
    tertiary_color = models.CharField(max_length=16, null=True, blank=True)  # HEX color
    home_kit = models.ImageField(
        upload_to="teams/kits/england/manchester_united/home_kit.png",
        null=True,
        blank=True,
    )
    away_kit = models.ImageField(
        upload_to="teams/kits/england/manchester_united/away_kit.png",
        null=True,
        blank=True,
    )
    third_kit = models.ImageField(
        upload_to="teams/kits/england/manchester_united/third_kit.png",
        null=True,
        blank=True,
    )
    official_website = models.URLField(max_length=200, null=True, blank=True)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    twitter = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)


# Using both null=True and blank=True is common for non-string fields when you want to allow the field to be optional both at the form levyel (no validation error for empty values) and at the database level (storing an actual NULL value).
