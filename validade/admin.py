from django.contrib import admin
from .models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 
                    'descricao', 
                    'qtd_entrada', 
                    'qtd_atual', 
                    'data_fabricacao', 
                    'data_validade']
    search_fields = ['nome']
