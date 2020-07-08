"""
To execute this script you need to run "python manage.py shell" and inside shell run the command
" exec(open('script.py').read())"
The csv file need to be processed to match the django model.
This script needs no headers in oreder to run.
"""
import csv
from fixtures.models import GermanFixtures

CSV='D1.csv'

with open(CSV, newline='') as csvfile:
	reader=csv.reader(csvfile, delimiter=',')
	next(reader)
	for row in reader:
		# EnglandFixtures.objects.create(hometeam=row[0],awayteam=row[1],homegoals=row[2],awaygoals=row[3])
		# JapanFixtures.objects.create(season=row[0],hometeam=row[1],awayteam=row[2],homegoals=row[3],awaygoals=row[4])
		GermanFixtures.objects.create(season=row[0],hometeam=row[1],awayteam=row[2],homegoals=row[3],awaygoals=row[4])