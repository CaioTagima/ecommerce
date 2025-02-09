from django.db import models
from django.contrib.auth.models import User


class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Usuário')
    total = models.FloatField()
    status = models.CharField(
        default="C",
        max_length=1,
        choices=(
            ('C', 'Criado'),
            ('A', 'Aprovado'),
            ('R', 'Reprovado'),
            ('P', 'Pendente'),
            ('E', 'Enviado'),
            ('F', 'Finalizado'),
        )
    )

    def __str__(self):
        return f'Pedido Número: {self.pk}'

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.CharField(max_length=255)
    produto_id = models.PositiveIntegerField(verbose_name='ID')
    variacao = models.CharField(max_length=255,verbose_name='Variação')
    variacao_id = models.PositiveBigIntegerField(verbose_name='Variação ID')
    preco = models.FloatField(verbose_name='Preço')
    preco_promocional = models.FloatField(default=0,verbose_name='Preço Promocional')
    quantidade = models.PositiveIntegerField()
    imagem = models.CharField(max_length=2550)

    def __str__(self):
        return f'Item do {self.pedido} Número: {self.pk}'
    
    class Meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Itens do pedido'