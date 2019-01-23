from django.conf.urls import patterns, url
from views import RegistrarUsuarioView

"""
Utilizando RegistrarUsuarioView.as_view()
"""

urlpatterns = patterns('',
    url(r'^registrar/$', RegistrarUsuarioView.as_view(), name='registrar'),
)