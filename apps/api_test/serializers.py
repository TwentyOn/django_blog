from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Book
        read_only_fields = ['id']
