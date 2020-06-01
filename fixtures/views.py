from fixtures.models import Fixtures
from fixtures.serializers import FixturesSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .forms import FixtureForms
from django.contrib import messages


from fixtures.teams import TEAM_CHOICES

from django.shortcuts import render

import pandas as pd
import numpy as np
from scipy.stats import poisson, skellam
import statsmodels.api as sm



class FixtureList(APIView):
    """
    List all fixtures, or create a new fixture.
    """
    def get(self, request, format=None):
        fixtures = Fixtures.objects.all()
        serializer = FixturesSerializer(fixtures, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FixturesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FixtureDetail(APIView):
    """
    Retrieve , update or delete a fixture instance.
    """
    def get_object(self, pk):
        try:
            return Fixtures.objects.get(pk=pk)
        except Fixtures.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        fixture = self.get_object(pk)
        serializer = FixturesSerializer(fixture)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        fixture = self.get_object(pk)
        serializer = FixturesSerializer(fixture, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        fixture = self.get_object(pk)
        fixture.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def index(request):
    fixture_list = Fixtures.objects.all()
    context = {'fixture_list': fixture_list,
               'Teams': TEAM_CHOICES,
               }
    return render(request, 'fixtures/index.html', context)


def simulate_match(foot_model, homeTeam, awayTeam, max_goals=10):
    home_goals_avg = foot_model.predict(pd.DataFrame(data={'team': homeTeam, 'opponent': awayTeam, 'home': 1}, index=[1])).values[0]
    away_goals_avg = foot_model.predict(pd.DataFrame(data={'team': awayTeam, 'opponent': homeTeam, 'home': 0}, index=[1])).values[0]

    team_pred = [[poisson.pmf(i, team_avg) for i in range(0, max_goals+1)] for team_avg in[home_goals_avg, away_goals_avg]]
    return(np.outer(np.array(team_pred[0]), np.array(team_pred[1])))


def calculate(request):
    if request.method == 'POST':
        form = FixtureForms(request.POST)
        if form.is_valid():
            hometeam = form.cleaned_data['hometeam']
            awayteam = form.cleaned_data['awayteam']
            print(hometeam, awayteam)
            print("Hello")
            poisson_model = sm.load('goal.pickle')
            match = simulate_match(poisson_model, hometeam, awayteam, max_goals=10)
            goalgoal = round((np.sum(match[1:, 1:])), 3),"%"
            messages.success(request, 'Goal/Goal: {}'.format(goalgoal))
    form = FixtureForms()
    return render(request, 'fixtures/calculate.html', {'form': form})


