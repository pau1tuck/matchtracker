from django.db import models


class Competition(models.Model):
    competition_number = models.IntegerField()
    name = models.CharField(max_length=128)
    description = models.TextField()
    logo = models.ImageField(upload_to="competitions/")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
