from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    nomeUsuario = models.CharField('nomeUsuario', max_length=200)
    emailUusario = models.CharField('emailUusario', max_length=200)
    senhaUsuario = models.IntergeFilder('senhaUsuario')

    def __str__(self):
        return '{}'.format(self.nomeUsuario)

class Projeto(models.Model):
	nomeProjeto - Models.CharField('nomeProjeto', max_length=200)

	def __str__(self):
		return '{}'.format(self .nomeProjeto)

class UsuarioProjeto(models.Model):
	projeto = models.ForeignKey('Projeto')
	usuario = models.ForeignKey('Usuario')

	def __str__(self):
        return '{}'.format(self.usuario)

class Tarefa(models.Model):
	nomeTarefa = models.CharField('nomeTarefa', max_length=200)
	dataEhoraDeinicio = models.DateTimeField('dataEhoraDeinicio', default=timezone.now)
	projeto = models.ForeignKey('Projeto')
	usuario = models.ForeignKey('Usuario')

	def __str__(self):
        return '{}'.format(self.nomeTarefa)
		
