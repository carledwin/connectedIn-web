from django.db import models

# Create your models here.

#class Perfil(object):

# model.Model criara uma tabela no banco com colunas com nomes e tipos dos atributos
class Perfil(models.Model):

	#por nao herdar de object nao precisa do construtor abaixo
	#def __init__(self, nome='', email='', telefone='', nome_empresa=''):
	#	self.nome = nome
	#	self.email = email
	#	self.telefone = telefone
	#	self.nome_empresa = nome_empresa

	nome = models.CharField(max_length=255, null=False)
	email = models.CharField(max_length=255, null=False)
	telefone = models.CharField(max_length=15, null=False)
	nome_empresa = models.CharField(max_length=255, null=False)