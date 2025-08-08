from django.urls import path, include
from .views import BookListAPIView

urlpatterns = [
    path('books/', BookListAPIView.as_view(), name='book-list'),
]
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename= 'book_all')
urlpatterns = [
    path('', include(router.urls)),
]

from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('token/', obtain_auth_token, name='api_token_auth'),
] # creates endpoint for token authentication
