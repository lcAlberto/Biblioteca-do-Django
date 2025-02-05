# Generated by Django 5.1.6 on 2025-02-05 18:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=100)),
                ('editora', models.CharField(max_length=100)),
                ('publicado_em', models.CharField(max_length=100)),
                ('disponivel_em', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_usuario', models.CharField(max_length=100)),
                ('emprestado_em', models.CharField(max_length=100)),
                ('devolvido_em', models.CharField(max_length=100)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livros.livro')),
            ],
        ),
    ]
