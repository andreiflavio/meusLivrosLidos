from rest_framework import routers
from .views import (LivroAPIViewSet, UsuarioAPIViewSet)

router = routers.DefaultRouter()

router.register(r'livro', LivroAPIViewSet, base_name='livro')
router.register(r'usuario', UsuarioAPIViewSet)