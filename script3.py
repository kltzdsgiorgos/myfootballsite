"""
To execute this script you need to run "python manage.py shell" and inside shell run the command
" exec(open('script.py').read())"
The csv file need to be processed to match the django model.
This script needs no headers in oreder to run.
"""
import csv
from fixtures.models import EnglandFixtures

CSV='E0.csv'

with open(CSV, newline='') as csvfile:
	reader=csv.reader(csvfile, delimiter=',')
	next(reader)
	for row in reader:
		EnglandFixtures.objects.create(hometeam=row[0],awayteam=row[1],homegoals=row[2],awaygoals=row[3])
