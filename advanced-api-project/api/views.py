from django.shortcuts import render
from .models import Author, Book
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'publication_year', 'author']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book-list') # redirect after creation

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'publication_year', 'author']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book-list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book-list')

from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import BookSerializer
from .permissions import IsAdminOrReadOnly

class BookCreateAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        if Books.objects.filter(title=title).exists():
            raise serializers.ValidationError("A book with this title already exists.")
        serializer.save()

class BookUpdateAPIView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class =  BookSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def perform_update(self, serializer):
        print(f"Updating book: {serializer.instance.title}")
        serializer.save()
        