from django.db import models

class Doador(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class ItemDoado(models.Model):
    nome_item = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome_item

class Campanha(models.Model):
    nome_campanha = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return self.nome_campanha

class Doacao(models.Model):
    doador = models.ForeignKey(Doador, on_delete=models.CASCADE)
    item = models.ForeignKey(ItemDoado, on_delete=models.CASCADE)
    campanha = models.ForeignKey(Campanha, on_delete=models.CASCADE)
    data_doacao = models.DateField()

    def __str__(self):
        return f'{self.doador} - {self.item} - {self.campanha}'
