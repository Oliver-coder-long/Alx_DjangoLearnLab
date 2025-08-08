from django.shortcuts import render

from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated
class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # only authenticated users can access the view
    



    
