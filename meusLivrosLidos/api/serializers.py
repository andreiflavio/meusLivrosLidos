from rest_framework import serializers
from meusLivrosLidos.livro.models import Livro
from django.contrib.auth.models import User


class LivroSerializer(serializers.ModelSerializer):
	
	def create(self, validated_data):		
		validated_data['user'] = self.context['request'].user
		return super().create(validated_data)
		

	class Meta:
		model = Livro
		fields = ['user', 'id', 'nome', 'autor', 'serie', 'num_paginas',
			'inicio', 'fim', 'nota', 'ebook', 'obs']


class UserSerializer(serializers.ModelSerializer):

	#Ao salvar usuário alterar o is_active para false, considerando que ele só será ativo após confirmação por e-mail 
	def create(self, validated_data):
		user = super().create(validated_data)
		user.is_active = False
		user.save()
		#Neste serializer terá envio de e-mail com link redirecionando para sistema e logando usuário.
		return user
		
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'username', 'is_active']