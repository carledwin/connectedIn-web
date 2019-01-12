from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # r'^$' --> raw string
    # url(r'^$', 'connectedIn.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'perfis.views.view_index'),
)
