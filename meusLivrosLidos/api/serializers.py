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
		
	class Meta:
		model = User
		fields = ['id', 'first_name', 'last_name', 'email', 'username', 'is_active']