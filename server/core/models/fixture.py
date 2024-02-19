from django.db import models


class Fixture(models.Model):
    season = models.CharField(max_length=100)
    date = models.DateField()
    week_number = models.IntegerField()
    time = models.TimeField()
    competition = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.competition} - {self.date} - {self.venue}"
