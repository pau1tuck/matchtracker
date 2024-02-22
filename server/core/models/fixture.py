from django.db import models
from .competition import Competition
from .team import Team
from .stadium import Stadium


class Fixture(models.Model):
    season = models.CharField(max_length=16)
    date = models.DateField()
    week_number = models.IntegerField()
    time = models.TimeField()
    timestamp = models.DateTimeField()
    league = models.ForeignKey(
        Competition, on_delete=models.CASCADE, related_name="competition"
    )
    competition = models.CharField(max_length=128)
    venue = models.foreign_key(
        Stadium, on_delete=models.CASCADE, related_name="stadium"
    )
    referee = models.CharField(max_length=128)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team")
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team")
    first_name = mode.
    def __str__(self):
        return f"{self.competition} - {self.date} - {self.venue}"
