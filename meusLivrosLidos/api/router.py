from rest_framework import routers
from .views import (LivroAPIViewSet, UsuarioAPIViewSet)

router = routers.DefaultRouter()

router.register(r'livros', LivroAPIViewSet, base_name='livros')
router.register(r'usuario', UsuarioAPIViewSet)