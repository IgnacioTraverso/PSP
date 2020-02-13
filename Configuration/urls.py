from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .views import *

urlpatterns = [
   path('crear_player/', staff_member_required(login_required(crearPlayer)), name ='crear_player'),
   path('listar_player/',staff_member_required(login_required(listarPlayer)), name='listar_player'),
   path('editar_player/<int:id>',staff_member_required(login_required(editarPlayer)), name='editar_player'),
   path('eliminar_player/<int:id>',staff_member_required(login_required(eliminarPlayer)), name='eliminar_player'),

   path('crear_owner/', staff_member_required(login_required(crearOwner.as_view())), name ='crear_owner'),
   path('listar_owner/',login_required(listarOwner.as_view()), name='listar_owner'),
   path('editar_owner/<int:pk>',staff_member_required(login_required(editarOwner.as_view())), name='editar_owner'),
   path('eliminar_owner/<int:pk>',staff_member_required(login_required(eliminarOwner.as_view())), name='eliminar_owner'),

   path('crear_team/', staff_member_required(login_required(crearTeam.as_view())), name ='crear_team'),
   path('listar_team/',login_required(listarTeam.as_view()), name='listar_team'),
   path('editar_team/<int:pk>',staff_member_required(login_required(editarTeam.as_view())), name='editar_team'),
   path('eliminar_team/<int:pk>',staff_member_required(login_required(eliminarTeam.as_view())), name='eliminar_team'),

   path('crear_tournament/', staff_member_required(login_required(crearTournament.as_view())), name ='crear_tournament'),
   path('listar_tournament/',login_required(listarTournament.as_view()), name='listar_tournament'),
   path('editar_tournament/<int:pk>',staff_member_required(login_required(editarTournament.as_view())), name='editar_tournament'),
   path('eliminar_tournament/<int:pk>',staff_member_required(login_required(eliminarTournament.as_view())), name='eliminar_tournament'),

   path('crear_tournamentteam/', staff_member_required(login_required(crearTournamentTeam.as_view())), name ='crear_tournamentteam'),
   path('listar_tournamentteam/',login_required(listarTournamentTeam.as_view()), name='listar_tournamentteam'),
   path('editar_tournamentteam/<int:pk>',staff_member_required(login_required(editarTournamentTeam.as_view())), name='editar_tournamentteam'),
   path('eliminar_tournamentteam/<int:pk>',staff_member_required(login_required(eliminarTournamentTeam.as_view())), name='eliminar_tournamentteam'),

]