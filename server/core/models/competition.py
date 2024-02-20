from django.db import models


class Competition(models.Model):
    competition_id = models.IntegerField()
    name = models.CharField(max_length=128)
    season = models.CharField(max_length=16)
    round = models.CharField(max_length=32)
    description = models.TextField()
    logo = models.ImageField(upload_to="media/competitions/")
    flag = models.ImageField(upload_to="media/flags/")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()