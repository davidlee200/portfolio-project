from django import forms
from .models import long_game_practice




class long_game_practice_form(forms.Form):
    # your_name = forms.CharField(label='Your name', max_length=100)
    date_of_practice = forms.DateField()
    number_of_balls = forms.IntegerField()
