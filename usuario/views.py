from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView, FormView
from django.contrib.auth import login,logout
from django.http import HttpResponseRedirect
from .forms import FormularioLogin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')

    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,**kwargs)

    def form_valid(self,form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

class RegistroUsuario(CreateView):
    model = User
    template_name = 'usuario/registrar.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('index')
