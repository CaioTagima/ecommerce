from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse

class Pagar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Pagar')

class Detalhes(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhes')

class SalvarPedido(View):
    def get(self, *args, **kwargs):
        return HttpResponse('FecharPedido')

