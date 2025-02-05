from django.db import models

# Create your models here.

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    publicado_em = models.CharField(max_length=100)
    disponivel_em = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    nome_usuario = models.CharField(max_length=100)
    emprestado_em = models.CharField(max_length=100)
    devolvido_em = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome_usuario} pegou {self.livro.titulo} em {self.emprestado_em}"
