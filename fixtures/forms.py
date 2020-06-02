from django import forms


class FixtureForms(forms.Form):
    hometeam = forms.CharField(max_length=25)
    awayteam = forms.CharField(max_length=25)
    # homegoals = forms.IntegerField()
    # awaygoals = forms.IntegerField()