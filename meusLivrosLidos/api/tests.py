from django.test import TestCase
from django.urls import reverse
#from rest_framework.test import APIRequestFactory
from django.urls import reverse

from rest_framework import status

class TestRestAPILivro(TestCase):

	#def setUp(self):
		#self.factory = APIRequestFactory()		
		

	# def test_api_livro_create(self):		
	# 	data = { 
	# 			'user': 'Usuário teste',
	# 			'nome': 'Livro teste', 
	# 			'autor': 'Novo autor'
	# 		}

	# 	response = self.factory.post('/livros/', data,  format='json')		
	# 	self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_api_livro_create(self):
		base_url = reverse('api/livros')	
		data = { 
				'user': 'Usuário teste',
				'nome': 'Livro teste', 
				'autor': 'Novo autor'
			}
		response = self.client.post(self.base_url,data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
