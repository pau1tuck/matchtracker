from django.db import models
from .stadium import Stadium
from .competition import Competition


class Team(models.Model):
    name = models.CharField(max_length=128)
    founded = models.Integer()
    logo = models.ImageField(upload_to="teams/logos/")
    stadium = models.ForeignKey(
        Stadium, on_delete=models.CASCADE, related_name="Stadium"
    )
    competitions = models.ManyToManyField(Competition, related_name="competitions")
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    founded_year = models.IntegerField(null=True, blank=True)
    manager = models.CharField(max_length=128, null=True, blank=True)
    primary_color = models.CharField(max_length=7, null=True, blank=True)  # HEX color
    secondary_color = models.CharField(max_length=7, null=True, blank=True)  # HEX color
    official_website = models.URLField(max_length=200, null=True, blank=True)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    twitter = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)
