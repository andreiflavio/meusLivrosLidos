from .router import router
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
#from django.contrib.auth.decorators import login_required

app = 'api'

urlpatterns = [
	path('', include(router.urls)),
	path('login/', obtain_jwt_token),
    path('refresh-token/', refresh_jwt_token),
]