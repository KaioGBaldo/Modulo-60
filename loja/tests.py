from django.test import TestCase
from .models import Post

class PostIntegrityTest(TestCase):
    def test_criacao_post_e_slug_automatico(self):
        post = Post.objects.create(
            titulo="Meu Primeiro Post",
            conteudo="Conteúdo de teste",
            status="publicado"
        )
        self.assertEqual(post.slug, "meu-primeiro-post")
        self.assertEqual(Post.objects.count(), 1)
