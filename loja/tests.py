from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        # Cria um utilizador para testar a regra do autor
        self.user = User.objects.create_user(username='kaio', password='123')
        
    def test_criacao_postagem_com_slug_e_autor(self):
        # Testa Regras 1, 2, 3 e 5
        post = Post.objects.create(
            titulo="Minha Primeira Postagem",
            corpo="Conteúdo da postagem",
            autor=self.user
        )
        
        self.assertEqual(post.titulo, "Minha Primeira Postagem")
        self.assertEqual(post.slug, "minha-primeira-postagem") # Regra 2: Slug Automático
        self.assertEqual(post.autor.username, "kaio")         # Regra 5: Autor correto
        self.assertEqual(post.status, "rascunho")             # Regra 4: Default rascunho

    def test_status_publicado(self):
        # Testa Regra 4: Status de publicado
        post = Post.objects.create(
            titulo="Post Publicado",
            corpo="Texto",
            autor=self.user,
            status='publicado'
        )
        self.assertEqual(post.status, 'publicado')

    def test_slug_automatico_no_save(self):
        # Garante que mesmo sem passar o slug, o save() o gera
        post = Post(titulo="Teste de Slug", corpo="...", autor=self.user)
        post.save()
        self.assertEqual(post.slug, "teste-de-slug")
