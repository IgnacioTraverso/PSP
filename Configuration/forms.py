from django import forms
from .models import *

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['Name','FName','Nick','Age','Photo','ID_Team']

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['Name','FName','Age']
        labels = {
            'Name': 'Name',
            'FName': 'Family name',
            'Age': 'Age',
        }
        widgets = {
            'Name': forms.TextInput(
               attrs = {
                   'class':'form-control',
                   'placeholder':'Type the owners name',
                   'id':'Name'
               } 
            ),
            'FName': forms.TextInput(
               attrs = {
                   'class':'form-control',
                   'placeholder':'Type the owners family name',
                   'id':'FName'
               } 
            ),
            'Age': forms.NumberInput(
               attrs = {
                   'class':'form-control',
                   'placeholder':'Select Age',
                   'id':'Age'
               } 
            )
        }


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['Name','ID_Owner']
        labels = {
            'Name': 'Name',
            'ID_Owner': 'Id Owner',
        }
        widgets = {
            'Name': forms.TextInput(
               attrs = {
                   'class':'form-control',
                   'placeholder':'Type the owners name',
                   'id':'Name'
               } 
            ),
            'ID_Owner': forms.Select(
               attrs = {
                   'class':'form-control',
                   'placeholder':'Type the owners id',
                   'id':'ID_Owner'
               } 
            )
       }

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['Name','Pricepool','Winner','MVP']
        labels = {
            'Name': 'Name',
            'Pricepool': 'Pricepool',
            'Winner': 'Winner',
            'MVP': 'MVP',
        }
        widgets = {
            'Name': forms.TextInput(
               attrs = {
                   'class':'form-control',
                   'placeholder':'Type the tournaments name',
                   'id':'Name'
               } 
            ),
            'Pricepool': forms.NumberInput(
               attrs = {
                   'class':'form-control',
                   'placeholder':'Type the pricepool',
                   'id':'Pricepool'
               } 
            ),
            'Winner': forms.Select(
               attrs = {
                   'class':'form-control',
                   'placeholder':'Type the winners name',
                   'id':'Winner'
               } 
            ),
            'MVP': forms.Select(
               attrs = {
                   'class':'form-control',
                   'placeholder':'Type the mvp id',
                   'id':'MVP'
               } 
            )
        }

class TournamentTeamForm(forms.ModelForm):
    class Meta:
        model = TournamentTeam
        fields = ['ID_Tournament','ID_Team','Position']
        labels = {
            'ID_Tournament': 'ID_Tournament',
            'ID_Team': 'ID_Team',
            'Position': 'Position',
        }
        widgets = {
            'ID_Tournament': forms.Select(
               attrs = {
                   'class':'form-control',
                   'placeholder':'Type the tournaments name',
                   'id':'ID_Tournament'
                } 
            ),
            'ID_Team': forms.Select(
               attrs = {
                   'class':'form-control',
                   'placeholder':'Type the team name',
                   'id':'ID_Team'
                } 
            ),
            'Position': forms.NumberInput(
               attrs = {
                   'class':'form-control',
                   'placeholder':'Type the position',
                   'id':'Position'
                } 
            )
        }