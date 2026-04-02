from django.db import models

from core.models.modelo import Modelo
from core.models.cor import Cor
from core.models.acessorio import Acessorio

class Veiculo(models.Model):
    ano = models.IntegerField(null=True, blank=True, default=0)
    preco = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, default=0)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="veículos")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veículos")
    acessorios = models.ManyToManyField(Acessorio, related_name="veículos")

    class Meta:
        verbose_name = "veículo"
        verbose_name_plural = "veículos"

    def __str__(self):
        return f'({self.id}) {self.modelo} {self.cor} - {self.ano}'