from .models import Fixtures
from rest_framework import serializers


class FixturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fixtures
        fields = ['id', 'hometeam', 'awayteam', 'homegoals', 'awaygoals']