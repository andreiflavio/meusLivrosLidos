from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import LivroSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet
from meusLivrosLidos.livro.models import Livro


class LivroAPIViewSet(ModelViewSet):	
    serializer_class = LivroSerializer

    def get_queryset(self):
    	return Livro.objects.filter(user=self.request.user).order_by('-data_cadastro')
    


class UsuarioAPIViewSet(ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
