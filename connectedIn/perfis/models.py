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
	#convites_feitos
	#convites_recebidos

	def convidar(self, perfil_convidado):
		convite = Convite(solicitante=self, convidado=perfil_convidado).save()

#O Django controla related_name sao variaveis passadas para a classe Perfil, 
# fazendo como se estes atributos existissem nessa classe
class Convite(models.Model):
	solicitante = models.ForeignKey(Perfil, related_name='convites_feitos')
	convidado = models.ForeignKey(Perfil, related_name='convites_recebidos')		