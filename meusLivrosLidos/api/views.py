from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from .serializers import LivroSerializer, UserSerializer

from meusLivrosLidos.livro.models import Livro


class LivroAPIViewSet(ModelViewSet):	
    serializer_class = LivroSerializer

    def get_queryset(self):    	
    	queryset = Livro.objects.filter(user=self.request.user).order_by('-data_cadastro')
    	search = self.request.query_params.get('search', None)
    	if search is not None:
    		return queryset.filter(Q(nome__icontains=search) | Q(autor__icontains=search))
    	else:
    		return queryset
    

class UsuarioAPIViewSet(ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer