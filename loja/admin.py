from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Campos exibidos na lista
    list_display = ('titulo', 'slug', 'status', 'data_criacao')
    
    # Filtros laterais
    list_filter = ('status', 'data_criacao')
    
    # Campos de busca
    search_fields = ('titulo', 'conteudo')
    
    # Faz o slug ser preenchido automaticamente enquanto você digita o título no Admin
    prepopulated_fields = {'slug': ('titulo',)}
    
    # Permite editar o status diretamente na lista de posts
    list_editable = ('status',)
