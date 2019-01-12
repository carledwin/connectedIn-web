from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
#
def view_index(request):
    return HttpResponse("Bem vindo ao connectedIn")