from rest_framework import serializers
from .models import BookDetail,Books


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id','name','editor','publish','category']

class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookDetail
        fields = ['id','description','model_Book']