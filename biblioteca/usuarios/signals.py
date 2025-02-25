from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from .models import Usuario

@receiver(post_save, sender=Usuario)
def definir_permissoes(sender, instance, created, **kwargs):
    if created:
        if instance.tipo == Usuario.LEITOR:
            grupo, _ = Group.objects.get_or_create(name='Leitor')
        else:
            grupo, _ = Group.objects.get_or_create(name='Writer')

        instance.groups.add(grupo)
