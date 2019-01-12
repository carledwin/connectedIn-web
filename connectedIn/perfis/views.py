from django.shortcuts import render
#from django.http import HttpResponse
from perfis.models import Perfil


# Create your views here.
#
def view_index(request):
    #return HttpResponse("Bem vindo ao connectedIn")
    return render(request, 'index.html')

def view_perfil(request, perfil_id):

	# perfil = Perfil()

	#if perfil_id == '1':
	#	perfil = Perfil('Carl Edwin Antonio Nascimento', 'carl@email.com', '2222-4444', 'Alura')

	#if perfil_id == '2':
	#	perfil = Perfil('Albert', 'albert@email.com', '34334-6675', 'Sales')	

	perfil = Perfil.objects.get(id=perfil_id)

	return render(request, 'perfil.html', {'perfil':perfil})