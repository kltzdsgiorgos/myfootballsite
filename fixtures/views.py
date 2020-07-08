from fixtures.models import EnglandFixtures, JapanFixtures, GermanFixtures
from fixtures.serializers import EnglandFixturesSerializer, JapanFixturesSerializer, GermanFixturesSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .forms import FixtureForms
from django.contrib import messages, auth

from django.contrib.auth import authenticate
from fixtures.teams import TEAM_CHOICES

from django.shortcuts import render, redirect

import pandas as pd
import numpy as np
from scipy.stats import poisson
import statsmodels.api as sm


class EnglandFixtureList(APIView):

    def get(self, request, format=None):
        fixtures = EnglandFixtures.objects.all()
        serializer = EnglandFixturesSerializer(fixtures, many=True)
        return Response(serializer.data)

# this method is currently not used but could be for future uses
#     def post(self, request, format=None):
#         serializer = EnglandFixturesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class used fot a particular fixture
# class EnglandFixtureDetail(APIView):
#     """
#     Retrieve , update or delete a fixture instance.
#     """
#     def get_object(self, pk):
#         try:
#             return EnglandFixtures.objects.get(pk=pk)
#         except EnglandFixtures.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         fixture = self.get_object(pk)
#         serializer = EnglandFixturesSerializer(fixture)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         fixture = self.get_object(pk)
#         serializer = EnglandFixturesSerializer(fixture, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         fixture = self.get_object(pk)
#         fixture.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class GermanFixtureList(APIView):

    def get(self, request, format=None):
        fixtures = GermanFixtures.objects.all()
        serializer = GermanFixturesSerializer(fixtures, many=True)
        return Response(serializer.data)


class JapanFixtureList(APIView):

    def get(self, request, format=None):
        fixtures = JapanFixtures.objects.all()
        serializer = JapanFixturesSerializer(fixtures, many=True)
        return Response(serializer.data)


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    fixture_list = EnglandFixtures.objects.all()
    context = {'fixture_list': fixture_list,
               'Teams': TEAM_CHOICES,
               }
    return render(request, 'home.html', context)


def japan(request):
    return render(request, 'japan.html')


def german(request):
    return render(request, 'german.html')


def england(request):
    return render(request, 'england.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # messages.success(request, "You are now logged in") # there is a bug with emssages
            return redirect('home')
        else:
            # messages.error(request, "Invalid Credentials") # # there is a bug with emssages
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        # messages.success(request, "You are now logged out") # there is a bug with emssages
    return redirect('login')


def simulate_match(foot_model, homeTeam, awayTeam, max_goals=10):
    home_goals_avg = foot_model.predict(pd.DataFrame(data={'team': homeTeam, 'opponent': awayTeam, 'home': 1}, index=[1])).values[0]
    away_goals_avg = foot_model.predict(pd.DataFrame(data={'team': awayTeam, 'opponent': homeTeam, 'home': 0}, index=[1])).values[0]

    team_pred = [[poisson.pmf(i, team_avg) for i in range(0, max_goals+1)] for team_avg in[home_goals_avg, away_goals_avg]]
    return(np.outer(np.array(team_pred[0]), np.array(team_pred[1])))


def calculategerman(request):
    if request.method == 'POST':
        form = FixtureForms(request.POST)
        if form.is_valid():
            hometeam = form.cleaned_data['hometeam']
            awayteam = form.cleaned_data['awayteam']
            print(hometeam, awayteam)
            print("Hello")
            poisson_model = sm.load('German.pickle')
            match = simulate_match(poisson_model, hometeam, awayteam, max_goals=10)
            goalgoal = round((np.sum(match[1:, 1:])), 3), "%"
            over = round((np.sum(match[2:])+np.sum(match[:2, 2:])-np.sum(match[2:3, 0])-np.sum(match[0:1, 2])), 3), "%"
            messages.success(request, 'Goal/Goal: {}'.format(goalgoal))
            messages.success(request, 'Over 2.5: {}'.format(over))
    form = FixtureForms()
    return render(request, 'calculategerman.html', {'form': form})


def calculatejapan(request):
    if request.method == 'POST':
        form = FixtureForms(request.POST)
        if form.is_valid():
            hometeam = form.cleaned_data['hometeam']
            awayteam = form.cleaned_data['awayteam']
            print(hometeam, awayteam)
            print("Hello")
            poisson_model = sm.load('Japan.pickle')
            match = simulate_match(poisson_model, hometeam, awayteam, max_goals=10)
            goalgoal = round((np.sum(match[1:, 1:])), 3), "%"
            over = round((np.sum(match[2:])+np.sum(match[:2, 2:])-np.sum(match[2:3, 0])-np.sum(match[0:1, 2])), 3), "%"
            messages.success(request, 'Goal/Goal: {}'.format(goalgoal))
            messages.success(request, 'Over 2.5: {}'.format(over))
    form = FixtureForms()
    return render(request, 'calculateJapan.html', {'form': form})


def calculateengland(request):
    if request.method == 'POST':
        form = FixtureForms(request.POST)
        if form.is_valid():
            hometeam = form.cleaned_data['hometeam']
            awayteam = form.cleaned_data['awayteam']
            print(hometeam, awayteam)
            print("Hello")
            poisson_model = sm.load('England.pickle')
            match = simulate_match(poisson_model, hometeam, awayteam, max_goals=10)
            goalgoal = round((np.sum(match[1:, 1:])), 3), "%"
            over = round((np.sum(match[2:])+np.sum(match[:2, 2:])-np.sum(match[2:3, 0])-np.sum(match[0:1, 2])), 3), "%"
            messages.success(request, 'Goal/Goal: {}'.format(goalgoal))
            messages.success(request, 'Over 2.5: {}'.format(over))
    form = FixtureForms()
    return render(request, 'calculateengland.html', {'form': form})


