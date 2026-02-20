from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'autor', 'status')
    prepopulated_fields = {'slug': ('titulo',)} # Auxilia a Regra 2 no painel

    def save_model(self, request, obj, form, change):
        # Regra 5: Define o autor como o usuário logado
        if not obj.pk: 
            obj.autor = request.user
        super().save_model(request, obj, form, change)
