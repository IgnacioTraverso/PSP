from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
   path('crear_player/', login_required(crearPlayer), name ='crear_player'),
   path('listar_player/',login_required(listarPlayer), name='listar_player'),
   path('editar_player/<int:id>',login_required(editarPlayer), name='editar_player'),
   path('eliminar_player/<int:id>',login_required(eliminarPlayer), name='eliminar_player'),

   path('crear_owner/', login_required(crearOwner.as_view()), name ='crear_owner'),
   path('listar_owner/',login_required(listarOwner.as_view()), name='listar_owner'),
   path('editar_owner/<int:pk>',login_required(editarOwner.as_view()), name='editar_owner'),
   path('eliminar_owner/<int:pk>',login_required(eliminarOwner.as_view()), name='eliminar_owner'),

   path('crear_team/', login_required(crearTeam.as_view()), name ='crear_team'),
   path('listar_team/',login_required(listarTeam.as_view()), name='listar_team'),
   path('editar_team/<int:pk>',login_required(editarTeam.as_view()), name='editar_team'),
   path('eliminar_team/<int:pk>',login_required(eliminarTeam.as_view()), name='eliminar_team'),

   path('crear_tournament/', login_required(crearTournament.as_view()), name ='crear_tournament'),
   path('listar_tournament/',login_required(listarTournament.as_view()), name='listar_tournament'),
   path('editar_tournament/<int:pk>',login_required(editarTournament.as_view()), name='editar_tournament'),
   path('eliminar_tournament/<int:pk>',login_required(eliminarTournament.as_view()), name='eliminar_tournament'),

   path('crear_tournamentteam/', (crearTournamentTeam.as_view()), name ='crear_tournamentteam'),
   path('listar_tournamentteam/',(listarTournamentTeam.as_view()), name='listar_tournamentteam'),
   path('editar_tournamentteam/<int:pk>',(editarTournamentTeam.as_view()), name='editar_tournamentteam'),
   path('eliminar_tournamentteam/<int:pk>',(eliminarTournamentTeam.as_view()), name='eliminar_tournamentteam'),

]