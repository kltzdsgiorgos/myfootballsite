from django.db import models


class EnglandFixtures(models.Model):

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

    season = models.CharField(max_length=20)
    hometeam = models.CharField(max_length=25, choices=TEAM_CHOICES, blank=False)
    awayteam = models.CharField(max_length=25, choices=TEAM_CHOICES, blank=False)
    # hometeam = models.CharField(max_length=25, blank=False)
    # awayteam = models.CharField(max_length=25, blank=False)
    homegoals = models.IntegerField()
    awaygoals = models.IntegerField()

    def __str__(self):
        return '{} vs {}'.format(self.hometeam, self.awayteam)


class JapanFixtures(models.Model):

    season = models.CharField(max_length=20)
    hometeam = models.CharField(max_length=25, blank=False)
    awayteam = models.CharField(max_length=25, blank=False)
    homegoals = models.IntegerField()
    awaygoals = models.IntegerField()

    def __str__(self):
        return '{} vs {}'.format(self.hometeam, self.awayteam)


class GermanFixtures(models.Model):

    season = models.CharField(max_length=20)
    hometeam = models.CharField(max_length=25, blank=False)
    awayteam = models.CharField(max_length=25, blank=False)
    homegoals = models.IntegerField()
    awaygoals = models.IntegerField()

    def __str__(self):
        return '{} vs {}'.format(self.hometeam, self.awayteam)
