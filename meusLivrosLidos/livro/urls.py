from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .views import (LivroListView,
                    LivroAboutView,
                    LivroCreate,
                    LivroUpdate,
                    LivroDelete)                    

app_name="livro"

urlpatterns = [
    # path('/', LoginView.as_view(), name='login'),    
    path('', login_required(LivroListView.as_view()), name='livro-list'),
    path('about/<int:pk>', login_required(LivroAboutView.as_view()), name='livro-about'),
    path('create', login_required(LivroCreate.as_view()), name='livro-create'),
    path('update/<int:pk>', login_required(LivroUpdate.as_view()), name='livro-update'),
    path('delete/<int:pk>', login_required(LivroDelete.as_view()), name='livro-delete'),
]