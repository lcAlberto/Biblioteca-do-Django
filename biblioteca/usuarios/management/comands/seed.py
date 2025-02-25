from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from usuarios.models import Usuario
from livros.models import Livro, Emprestimo
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Popula o banco de dados com usuários, livros e empréstimos.'

    def handle(self, *args, **kwargs):
        # Criando grupos
        leitor_group, _ = Group.objects.get_or_create(name='LEITOR')
        writer_group, _ = Group.objects.get_or_create(name='WRITER')

        # Criando usuários
        leitor = Usuario.objects.create_user(username='leitor_user', password='senha123')
        writer = Usuario.objects.create_user(username='writer_user', password='senha123')

        leitor.groups.add(leitor_group)
        writer.groups.add(writer_group)

        self.stdout.write(self.style.SUCCESS('Usuários criados com sucesso.'))

        # Criando livros
        livros = []
        for i in range(5):
            livro = Livro.objects.create(
                titulo=f"Livro {i+1}",
                autor=f"Autor {i+1}",
                ano_publicacao=2000 + i,
                disponivel=True
            )
            livros.append(livro)

        self.stdout.write(self.style.SUCCESS('Livros criados com sucesso.'))

        # Criando empréstimos para o usuário leitor
        for i in range(3):
            Emprestimo.objects.create(
                usuario=leitor,
                livro=random.choice(livros),
                data_emprestimo=timezone.now() - timezone.timedelta(days=random.randint(1, 10)),
                data_devolucao=timezone.now() + timezone.timedelta(days=random.randint(5, 15))
            )

        self.stdout.write(self.style.SUCCESS('Empréstimos criados com sucesso.'))