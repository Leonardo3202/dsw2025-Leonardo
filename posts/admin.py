from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('autor', 'aprovado', 'criado_em')
    list_filter = ('aprovado',)
    search_fields = ('titulo', 'mensagem')
