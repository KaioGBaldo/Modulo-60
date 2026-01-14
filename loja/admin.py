from django.contrib import admin
from .models import Produto, Estoque


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'criado_em')
    search_fields = ('nome',)
    list_filter = ('criado_em',)


@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('id', 'produto', 'quantidade', 'local')
    search_fields = ('produto__nome',)
    list_filter = ('local',)
