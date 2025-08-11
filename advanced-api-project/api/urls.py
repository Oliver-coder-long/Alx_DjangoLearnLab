from django.urls import path
from .views import BookListView, BookCreateView, BookDetailView, BookUpdateView, BookDeleteView, BookCreateAPIView, BookUpdateAPIView

urlpatterns = [
    path('books/', BookListView.as_view(), name = 'book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name = 'book-detail'),
    path('books/create/', BookCreateView.as_view(), name = 'book-create'),
    path('books/update/', BookUpdateView.as_view(), name = 'book-update'),
    path('books/delete/', BookDeleteView.as_view(), name = 'book-delete'),
    path('api/books/create/', BookCreateAPIView.as_view(), name = 'book-create-api'),
    path('api/books/<int:pk>/update/', BookUpdateAPIView.as_view(), name = 'book-update-api'),
]
