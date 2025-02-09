from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import models



class BasePerfil(View):
    template_name = 'perfil/criar.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        if self.request.user.is_authenticated:
            self.contexto = {
                'userform': forms.UserForm(
                    data=self.request.POST or None,
                    usuario=self.request.user,
                    isinstance = self.request.user,
                    ),
                'perfilform': forms.PerfilForm(data=self.request.POST or None)
                }
        else:
            self.contexto = {
                'userform': forms.UserForm(data=self.request.POST or None),
                'perfilform': forms.PerfilForm(data=self.request.POST or None)
                }

        self.rendenizar = render(self.request, self.template_name, self.contexto)
    
    def get(self, *args, **kwargs):
        return self.rendenizar


class Criar(BasePerfil):
    def get(self, *args, **kwargs):
        return self.rendenizar

class Login(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Login')

class Logout(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Logout')

class Atualizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Atualizar')

