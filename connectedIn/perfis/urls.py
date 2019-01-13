from django.conf.urls import patterns, include, url

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
    url(r'^$', 'perfis.views.view_index', name='index'),
    #url(r'^perfis/(?P<perfil_id>\d+)$', 'perfis.views.view_perfil'),
    url(r'^perfis/(?P<perfil_id>\d+)$', 'perfis.views.view_perfil', name='perfis'),
    
)
