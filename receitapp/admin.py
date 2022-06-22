from receitapp import models
from django.contrib import admin


@admin.register(models.Receita)
class ReceitaAdmin(admin.ModelAdmin):
    fields = [
        'nome',
        'ingrediente',
        'modo_preparo',
        'tempo_preparo',
        'categoria',
        'dificuldade',
        'imagem',
        'preparada'
    ]
    list_display = (
        'nome',
        'categoria',
        'dificuldade',
        'preparada'
    )
    list_filter = ('categoria',)


@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass
