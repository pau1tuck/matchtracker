from django.db import models


class Fixture(models.Model):
    season = models.CharField(max_length=16)
    date = models.DateField()
    timestamp = models.DateTimeField()
    week_number = models.IntegerField()
    time = models.TimeField()
    competition = models.CharField(max_length=128)
    venue = models.CharField(max_length=128)
    referee = models.Char(max_length=128)

    def __str__(self):
        return f"{self.competition} - {self.date} - {self.venue}"
