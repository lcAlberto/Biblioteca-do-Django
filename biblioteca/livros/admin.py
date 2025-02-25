# from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Livro, Autor, Emprestimo

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'publicado_em', 'disponivel_em', 'editora')
    search_fields = ('titulo',)
    list_filter = ('publicado_em',)

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('livro', 'nome_usuario', 'emprestado_em', 'devolvido_em')
    list_filter = ('emprestado_em',)
