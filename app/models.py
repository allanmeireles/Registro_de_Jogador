from django.db import models

#Classe que define um modelo de registro de jogador.
class playerRegister(models.Model): 
    idade = models.IntegerField(max_length=100)
    time = models.CharField(max_length=150)
    jersey_number = models.IntegerField(max_length=99)
    nacionalidade= models.CharField(max_length=150) 
    posição = models.CharField(max_length=100)


