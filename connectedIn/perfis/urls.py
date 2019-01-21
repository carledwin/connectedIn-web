from django.conf.urls import patterns, include, url
from perfis import views
#import de views para nao precisar chamar o nome completo 'perfis.view.view_convidar'

urlpatterns = patterns('',
    # Examples:
    # r'^$' --> raw string
    # url(r'^$', 'connectedIn.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # ^comeca com 
    # $ termina com
    # \d+ com um ou mais digitos
    #url(r'^perfis/\d+$', 'perfis.views.view_perfil'),
    # grupo (?P<parm>\d+)
    url(r'^$', views.view_index, name='index'),
    url(r'^perfis/(?P<perfil_id>\d+)$', views.view_perfil, name='perfis'),
    url(r'^perfis/(?P<perfil_id>\d+)/convidar$', views.view_convidar, name='convidar'),
    url(r'^convite/(?P<convite_id>\d+)/aceitar$', views.view_aceitar, name='aceitar'),
    #url(r'^$', 'perfis.views.view_index', name='index'),
    #url(r'^perfis/(?P<perfil_id>\d+)$', 'perfis.views.view_perfil', name='perfis'),
    #url(r'^perfis/(?P<perfil_id>\d+)$', 'perfis.views.view_perfil'),
    #url(r'^perfis/(?P<perfil_id>\d+)/convidar$', 'perfis.view.view_convidar', name='convidar'),
)
