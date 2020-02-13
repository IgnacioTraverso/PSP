from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import *
from .models import *
from django.views.generic import *
from django.urls import reverse_lazy
# Create your views here.
class Inicio(TemplateView):
    template_name = "index.html"
# Players (en funciones)


def listarPlayer(request):
    players= Player.objects.all()
    return render(request, 'configuration/listar_player.html', {'players':players})

def crearPlayer(request):
    if request.method == 'POST':
        player_form = PlayerForm(request.POST, request.FILES or None)
        if player_form.is_valid():
            
            player_form.save()
            return redirect('Configuration:listar_player')
    else:
        player_form = PlayerForm()
    return render(request,'Configuration/crear_player.html',{'player_form':player_form})

def editarPlayer(request, id):
    player_form = None
    error = None
    try:
        player = Player.objects.get(id = id)
        if request.method == 'GET':
            player_form = PlayerForm( instance = player)
        else:
            player_form = PlayerForm(request.POST, instance= player)
            if player_form.is_valid():
                player_form.save()
            return redirect('index')
    except ObjectDoesNotExist as e:
        error = e
    return render(request,'Configuration/crear_player.html',{'player_form':player_form, 'error':error})

def eliminarPlayer(request, id):
    player = Player.objects.get(id=id)
    if request.method == 'POST':
        player.delete()
        return redirect('Configuration:listar_player')
    return render(request, 'configuration/eliminar_player.html', {'player':player})

#Owner

class listarOwner(ListView):
    model = Owner
    template_name = 'configuration/listar_owner.html'
    context_object_name = 'owners'
    queryset = Owner.objects.all()
    
class editarOwner(UpdateView):
    model = Owner
    form_class=OwnerForm
    success_url = reverse_lazy('Configuration:listar_owner')

class crearOwner(CreateView):
    model = Owner
    form_class=OwnerForm
    success_url = reverse_lazy('Configuration:listar_owner')

class eliminarOwner(DeleteView):
    model = Owner
    success_url = reverse_lazy('Configuration:listar_owner')


#Team

class listarTeam(ListView):
    model = Team
    template_name = 'configuration/listar_team.html'
    context_object_name = 'teams'
    queryset = Team.objects.all()
    
class editarTeam(UpdateView):
    model = Team
    form_class=TeamForm
    success_url = reverse_lazy('Configuration:listar_team')

class crearTeam(CreateView):
    model = Team
    form_class=TeamForm
    success_url = reverse_lazy('Configuration:listar_team')

class eliminarTeam(DeleteView):
    model = Team
    success_url = reverse_lazy('Configuration:listar_team')


#Tournament

class listarTournament(ListView):
    model = Tournament
    template_name = 'configuration/listar_tournament.html'
    context_object_name = 'tournaments'
    queryset = Tournament.objects.all()
    
class editarTournament(UpdateView):
    model = Tournament
    form_class=TournamentForm
    success_url = reverse_lazy('Configuration:listar_tournament')

class crearTournament(CreateView):
    model = Tournament
    form_class=TournamentForm
    success_url = reverse_lazy('Configuration:listar_tournament')

class eliminarTournament(DeleteView):
    model = Tournament
    success_url = reverse_lazy('Configuration:listar_tournament')


#TournamentTeam

class listarTournamentTeam(ListView):
    model = TournamentTeam
    template_name = 'configuration/listar_tournamentteam.html'
    context_object_name = 'tournamentteams'
    queryset = TournamentTeam.objects.all()
    
class editarTournamentTeam(UpdateView):
    model = TournamentTeam
    form_class=TournamentTeamForm
    success_url = reverse_lazy('Configuration:listar_tournamentteam')

class crearTournamentTeam(CreateView):
    model = TournamentTeam
    form_class=TournamentTeamForm
    success_url = reverse_lazy('Configuration:listar_tournamentteam')

class eliminarTournamentTeam(DeleteView):
    model = TournamentTeam
    success_url = reverse_lazy('Configuration:listar_tournamentteam')







