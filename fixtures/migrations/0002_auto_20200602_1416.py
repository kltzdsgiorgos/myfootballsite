# Generated by Django 3.0.6 on 2020-06-02 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixtures', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixtures',
            name='awayteam',
            field=models.CharField(choices=[('Arsenal', 'Arsenal'), ('Aston Villa', 'Aston Villa'), ('Burnley', 'Burnley'), ('Brighton', 'Brighton'), ('Bournemouth', 'Bournemouth'), ('Chelsea', 'Chelsea'), ('Crystal Palace', 'Crystal Palace'), ('Everton', 'Everton'), ('Liverpool', 'Liverpool'), ('Leicester', 'Leicester'), ('Newcastle', 'Newcastle'), ('Man City', 'Man City'), ('Man Utd', 'Man Utd'), ('Norwich', 'Norwich'), ('Wolves', 'Wolves'), ('Sheffield Utd', 'Sheffield Utd'), ('Spurs', 'Spurs'), ('Southampton', 'Southampton'), ('Watford', 'Watford'), ('West Ham', 'West Ham')], max_length=25),
        ),
        migrations.AlterField(
            model_name='fixtures',
            name='hometeam',
            field=models.CharField(choices=[('Arsenal', 'Arsenal'), ('Aston Villa', 'Aston Villa'), ('Burnley', 'Burnley'), ('Brighton', 'Brighton'), ('Bournemouth', 'Bournemouth'), ('Chelsea', 'Chelsea'), ('Crystal Palace', 'Crystal Palace'), ('Everton', 'Everton'), ('Liverpool', 'Liverpool'), ('Leicester', 'Leicester'), ('Newcastle', 'Newcastle'), ('Man City', 'Man City'), ('Man Utd', 'Man Utd'), ('Norwich', 'Norwich'), ('Wolves', 'Wolves'), ('Sheffield Utd', 'Sheffield Utd'), ('Spurs', 'Spurs'), ('Southampton', 'Southampton'), ('Watford', 'Watford'), ('West Ham', 'West Ham')], max_length=25),
        ),
    ]