from django.test import TestCase
from model_mommy import mommy
from meusLivrosLidos.livro.models import Livro
from django.contrib.auth.models import User


class TestRecord(TestCase):

	def setUp(self):
		self.user = mommy.make(User, username='User teste', password='12345')
		self.livro = mommy.make(Livro, user=self.user, nome='Livro TESTE', autor='Autor de teste')


	def test_livro_create(self):
		self.assertTrue(isinstance(self.livro, Livro))
		self.assertEquals(self.livro.__str__(),\
			self.livro.nome + ' - ' + self.livro.autor)

	def test_livro_update(self):
		nome_serie = 'Serie de teste'
		self.livro.serie = nome_serie
		self.livro.save()
		self.assertEquals(self.livro.serie, nome_serie)

	def test_livro_delete(self):
		count, livro = self.livro.delete()
		self.assertEquals(count, 1)

