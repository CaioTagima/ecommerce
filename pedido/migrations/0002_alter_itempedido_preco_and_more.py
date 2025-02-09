# Generated by Django 5.1.5 on 2025-02-06 23:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='itempedido',
            name='preco',
            field=models.FloatField(verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='itempedido',
            name='preco_promocional',
            field=models.FloatField(default=0, verbose_name='Preço Promocional'),
        ),
        migrations.AlterField(
            model_name='itempedido',
            name='produto_id',
            field=models.PositiveIntegerField(verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='itempedido',
            name='variacao',
            field=models.CharField(max_length=255, verbose_name='Variação'),
        ),
        migrations.AlterField(
            model_name='itempedido',
            name='variacao_id',
            field=models.PositiveBigIntegerField(verbose_name='Variação ID'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]
