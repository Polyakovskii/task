from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from .models import Book
from .serializers import BookSerializer, SingleBookSerializer
# Create your views here.

class BookView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({"books": serializer.data})
    def post(self, request):
        book = request.data.get('book')
        # Create an article from the above data
        serializer = SingleBookSerializer(data=book)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response({"success": "Book '{}' created successfully".format(book_saved.title)})

class SingleBookView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = SingleBookSerializer