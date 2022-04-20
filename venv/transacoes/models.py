from django.db import models

class Transacoes(models.Model):
    banco_origem = models.CharField(max_length=100)
    agencia_origem = models.IntegerField()
    conta_origem = models.CharField(max_length=10)
    banco_destino = models.CharField(max_length=100)
    agencia_destino = models.IntegerField()
    conta_destino = models.CharField(max_length=10)
    valor_transação = models.FloatField()
    data_hora_transacao = models.DateTimeField()
