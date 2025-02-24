from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework import generics
from rest_framework import viewsets
from .models import Book,User
from .serializers import BookSerializer,UserSerializer
# Create your views here.



class BookViewSet(viewsets.ModelViewSet):
    queryset= Book.objects.all()
    serializer_class = BookSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class= UserSerializer