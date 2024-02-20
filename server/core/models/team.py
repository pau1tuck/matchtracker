from django.db import models
from .stadium import Stadium
from .competition import Competition


class Team(models.Model):
    name = models.CharField(max_length=128)
    founded = models.Integer()
    logo = models.ImageField(upload_to="competitions/")
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE, related_name="Stadium")
    competitions = models.ManyToManyField(Competition, related_name='teams')