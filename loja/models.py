from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Post(models.Model):
    STATUS_CHOICES = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado'),
    )

    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    conteudo = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='rascunho')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_publicacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

# Signal para atualizar o slug automaticamente antes de salvar
@receiver(pre_save, sender=Post)
def gera_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.titulo)
