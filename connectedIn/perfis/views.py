from django.shortcuts import render, redirect
#from django.http import HttpResponse
from perfis.models import Perfil


# Create your views here.
#
def view_index(request):
    #return HttpResponse("Bem vindo ao connectedIn")
    return render(request, 'index.html', {'perfis': Perfil.objects.all()})

#palavra chave pass para nao dar erro em um metodo que ainda nao foi implementado 
def view_convidar(request, perfil_id):
	perfil_a_convidar = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	perfil_logado.convidar(perfil_a_convidar)
	return redirect(view_index)

def get_perfil_logado(request):
	return Perfil.objects.get(id=1)	

def view_perfil(request, perfil_id):

	# perfil = Perfil()

	#if perfil_id == '1':
	#	perfil = Perfil('Carl Edwin Antonio Nascimento', 'carl@email.com', '2222-4444', 'Alura')

	#if perfil_id == '2':
	#	perfil = Perfil('Albert', 'albert@email.com', '34334-6675', 'Sales')	

	perfil = Perfil.objects.get(id=perfil_id)

	return render(request, 'perfil.html', {'perfil':perfil})