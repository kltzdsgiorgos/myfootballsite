"""
To execute this script you need to run "python manage.py shell" and inside shell run the command
" exec(open('script.py').read())"
The csv file need to be processed to match the django model.
This script needs no headers in oreder to run.
"""
import csv
from fixtures.models import JapanFixtures

CSV='J1.csv'

with open(CSV, newline='') as csvfile:
	reader=csv.reader(csvfile, delimiter=',')
	next(reader)
	for row in reader:
		JapanFixtures.objects.create(season=row[0],hometeam=row[1],awayteam=row[2],homegoals=row[3],awaygoals=row[4])
