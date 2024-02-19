from django.db import models
from .competition import Competition
from .team import Team


class Fixture(models.Model):
    season = models.CharField(max_length=16)
    date = models.DateField()
    week_number = models.IntegerField()
    time = models.TimeField()
    timestamp = models.DateTimeField()
    league = models.ForeignKey(
        Competition, on_delete=models.CASCADE, related_name="Competition"
    )
    competition = models.CharField(max_length=128)
    venue = models.CharField(max_length=128)
    referee = models.CharField(max_length=128)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="Team")
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="Team")

    def __str__(self):
        return f"{self.competition} - {self.date} - {self.venue}"
