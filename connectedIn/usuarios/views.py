from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.

""" classBasedView herda de View para ter varios comportamentos padroes
para esta classe sempre precisamos definir dois metodos um get e um post
"""

class RegistrarUsuarioView(View):
    
    template_name = 'registrar.html'

    def get(self, request):
        # render para retornar a pagina
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)
