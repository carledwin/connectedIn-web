from django.conf.urls import patterns, include, url
from perfis import views
#import de views para nao precisar chamar o nome completo 'perfis.view.view_convidar'

urlpatterns = patterns('',
    url(r'^$', views.view_index, name='index'),
    url(r'^perfis/(?P<perfil_id>\d+)$', views.view_perfil, name='perfis'),
    url(r'^perfis/(?P<perfil_id>\d+)/convidar$', views.view_convidar, name='convidar'),
    url(r'^convite/(?P<convite_id>\d+)/aceitar$', views.view_aceitar, name='aceitar'),
)
