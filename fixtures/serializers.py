from .models import EnglandFixtures, JapanFixtures, GermanFixtures
from rest_framework import serializers


class EnglandFixturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnglandFixtures
        fields = ['id', 'season', 'hometeam', 'awayteam', 'homegoals', 'awaygoals']


class GermanFixturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GermanFixtures
        fields = ['id', 'season', 'hometeam', 'awayteam', 'homegoals', 'awaygoals']


class JapanFixturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = JapanFixtures
        fields = ['id', 'season', 'hometeam', 'awayteam', 'homegoals', 'awaygoals']
