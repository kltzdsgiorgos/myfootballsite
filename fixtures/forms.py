from django import forms


class FixtureForms(forms.Form):
    hometeam = forms.CharField(max_length=15)
    awayteam = forms.CharField(max_length=15)
    # homegoals = forms.IntegerField()
    # awaygoals = forms.IntegerField()