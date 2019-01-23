from django.shortcuts import render, redirect
from perfis.models import Perfil, Convite
from django.contrib.auth.decorators import login_required

@login_required
def view_index(request):
    return render(request, 'index.html', {'perfis': Perfil.objects.all(), 'perfil_logado': get_perfil_logado(request)})

@login_required
def view_convidar(request, perfil_id):
	perfil_a_convidar = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	perfil_logado.convidar(perfil_a_convidar)
	return redirect(view_index)

@login_required
def view_perfil(request, perfil_id):

	perfil = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	ja_eh_contato = perfil in perfil_logado.contatos.all()

	return render(request, 'perfil.html', {'perfil':perfil, 'ja_eh_contato':ja_eh_contato})

@login_required
def view_aceitar(request, convite_id):
	convite = Convite.objects.get(id=convite_id)
	convite.aceitar()
	return redirect('index') 

@login_required
def get_perfil_logado(request):
	#return Perfil.objects.get(id=1)
	'''
		O user eh disponibilizado pela sessao quando o mesmo estah logado
	'''	
	return request.user.perfil