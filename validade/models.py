from django.db import models
from django.utils import timezone

class Produto(models.Model):
    codigo = models.IntegerField(verbose_name='Código')
    nome = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255, verbose_name='Descrição')
    qtd_entrada = models.IntegerField(verbose_name='Quantidade Entrada')
    qtd_atual = models.IntegerField(verbose_name='Quantidade Atual')
    data_fabricacao = models.DateField(verbose_name='Data Fabricação')
    data_validade = models.DateField(verbose_name='Data Validade')

    def __str__(self):
        return self.nome

    def vencido(self):
        hoje = timezone.now().date()
        return self.data_validade < hoje

    def dias_restantes_validade(self):
        hoje = timezone.now().date()
        if hoje < self.data_validade:
            return (self.data_validade - hoje).days
        else:
            return 0