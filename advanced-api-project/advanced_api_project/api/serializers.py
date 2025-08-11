from rest_framework import serializers
from .models import Book, Author
from datetime import date
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'Book'
        fields = '__all__'
    
    def validate_publication_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("Publication date cannot be in the future.")
        return value



class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = 'Author'
        fields = ['name', 'books']

