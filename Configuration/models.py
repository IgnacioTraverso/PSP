from django.db import models 

# Create your models here.
class Owner(models.Model):
    Name=models.CharField(max_length=30)
    FName=models.CharField(max_length=30)
    Age=models.CharField(max_length=2)

    def __str__(self):
        cadena= "{0} {1}"
        return cadena.format(self.Name, self.FName)
   

class Team(models.Model):
    Name=models.CharField(max_length=30)
    ID_Owner=models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True) #many to one

    def __str__(self):
        cadena= "{0}"
        return cadena.format(self.Name)


class Player(models.Model):
    Name=models.CharField(max_length=30)
    FName=models.CharField(max_length=30)
    Nick=models.CharField(max_length=30)
    Age=models.CharField(max_length=2)
    Photo=models.ImageField(upload_to='fotos', blank=True, null=True)
    ID_Team=models.ForeignKey(Team, on_delete=models.SET_NULL, null=True) #many to one

    def __str__(self):
        cadena= "{0} {1} {2} {3}"
        return cadena.format('['+str(self.ID_Team)+']', self.Name, '"'+self.Nick+'"', self.FName)


class Tournament(models.Model):
    Name=models.CharField(max_length=30)
    Pricepool=models.CharField(max_length=10)
    Winner=models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)  #many to one
    MVP=models.ForeignKey(Player, on_delete=models.SET_NULL, null=True) #many to one

    def __str__(self):
        return self.Name

class TournamentTeam(models.Model):
    ID_Tournament=models.ForeignKey(Tournament, on_delete=models.SET_NULL, null=True)
    ID_Team=models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    Position=models.CharField(max_length=3)
    
    def __str__(self):
        cadena="{0} {1} {2}"
        return cadena.format(self.ID_Tournament,"and", self.ID_Team)

