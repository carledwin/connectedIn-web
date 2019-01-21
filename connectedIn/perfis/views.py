from django.shortcuts import render, redirect
#from django.http import HttpResponse
from perfis.models import Perfil, Convite

# Create your views here.
#
def view_index(request):
    #return HttpResponse("Bem vindo ao connectedIn")
    return render(request, 'index.html', {'perfis': Perfil.objects.all(), 'perfil_logado': get_perfil_logado(request)})

#palavra chave pass para nao dar erro em um metodo que ainda nao foi implementado 
def view_convidar(request, perfil_id):
	perfil_a_convidar = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	perfil_logado.convidar(perfil_a_convidar)
	return redirect(view_index)

def view_perfil(request, perfil_id):

	# perfil = Perfil()

	#if perfil_id == '1':
	#	perfil = Perfil('Carl Edwin Antonio Nascimento', 'carl@email.com', '2222-4444', 'Alura')

	#if perfil_id == '2':
	#	perfil = Perfil('Albert', 'albert@email.com', '34334-6675', 'Sales')	

	perfil = Perfil.objects.get(id=perfil_id)

	perfil_logado = get_perfil_logado(request)
	# vefica se o perfil logado esta contido na lista
	ja_eh_contato = perfil in perfil_logado.contatos.all()

	return render(request, 'perfil.html', {'perfil':perfil, 'ja_eh_contato':ja_eh_contato})

def view_aceitar(request, convite_id):
	convite = Convite.objects.get(id=convite_id)
	convite.aceitar()
	return redirect('index') 

def get_perfil_logado(request):
	return Perfil.objects.get(id=1)	