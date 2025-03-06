from rest_framework import serializers
from .models import Genre, Book, BookCopy, BookLending
from authors.models import Author


class GenreSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(many=True, queryset=Author.objects.all())
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all())

    class Meta:
        model = Genre
        fields = ['id', 'name', 'description']

    def validate_name(self, value):
        if len(value) > 50:
            raise serializers.ValidationError("Janr nomi 50 ta belgidan oshmasligi kerak.")
        if any(word in value.lower() for word in ['taqiqlangan', 'test']):
            raise serializers.ValidationError("Bu nomdan foydalanish mumkin emas.")
        return value


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre', 'published_date']

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Kitob nomi bo‘sh bo‘lishi mumkin emas.")
        return value


class BookCopySerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

    class Meta:
        model = BookCopy
        fields = [
            'id', 'book', 'inventory_number', 'condition',
            'is_available', 'added_date'
        ]


class BookLendingSerializer(serializers.ModelSerializer):
    book_copy = serializers.PrimaryKeyRelatedField(queryset=BookCopy.objects.all())

    class Meta:
        model = BookLending
        fields = '__all__'
