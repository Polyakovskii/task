from django.shortcuts import render

from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from .models import Book
from .serializers import BookSerializer
# Create your views here.

class BookView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SingleBookView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer