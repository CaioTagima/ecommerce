from django.contrib import admin
from . import models

class VariacaoInline(admin.TabularInline):
    model = models.Variacao
    extra = 1

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome','get_cifrado','get_cifrado_promo']
    inlines = [VariacaoInline]

admin.site.register(models.Produto, ProdutoAdmin)
admin.site.register(models.Variacao)