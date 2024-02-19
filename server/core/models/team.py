from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=128)
    logo = models.ImageField(upload_to="competitions/")
    founded = models.Integer()
