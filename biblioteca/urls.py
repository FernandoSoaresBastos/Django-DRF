from django.urls import path,include
from rest_framework.routers import DefaultRouter
from biblioteca.views import BookViewSet,UserViewSet

router = DefaultRouter()

router.register(r'livros',BookViewSet)
router.register(r'user',UserViewSet)

urlpatterns = [
    
    path('api/v1/',include(router.urls)),
]
