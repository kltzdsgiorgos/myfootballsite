from django.db import models


class Fixtures(models.Model):

    TEAM_CHOICES = (
        ('Arsenal', 'Arsenal'),
        ('Aston Villa', 'Aston Villa'),
        ('Burnley', 'Burnley'),
        ('Brighton', 'Brighton'),
        ('Bournemouth', 'Bournemouth'),
        ('Chelsea', 'Chelsea'),
        ('Crystal Palace', 'Crystal Palace'),
        ('Everton', 'Everton'),
        ('Liverpool', 'Liverpool'),
        ('Leicester', 'Leicester'),
        ('Newcastle', 'Newcastle'),
        ('Man City', 'Man City'),
        ('Man Utd', 'Man Utd'),
        ('Norwich', 'Norwich'),
        ('Wolves', 'Wolves'),
        ('Sheffield Utd', 'Sheffield Utd'),
        ('Spurs', 'Spurs'),
        ('Southampton', 'Southampton'),
        ('Watford', 'Watford'),
        ('West Ham', 'West Ham'),
    )

    hometeam = models.CharField(max_length=15, choices=TEAM_CHOICES, blank=False)
    awayteam = models.CharField(max_length=15, choices=TEAM_CHOICES, blank=False)
    homegoals = models.IntegerField()
    awaygoals = models.IntegerField()

    def __str__(self):
        return '{} vs {}'.format(self.hometeam, self.awayteam)
