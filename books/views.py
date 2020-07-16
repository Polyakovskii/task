from rest_framework import viewsets

from .models import Book
from .serializers import BookSerializer, SingleBookSerializer

class BookView(viewsets.GenericViewSet, viewsets.mixins.RetrieveModelMixin, viewsets.mixins.CreateModelMixin, viewsets.mixins.ListModelMixin):
    queryset = Book.objects.all()
    def get_serializer_class(self):
        if self.action == 'list':
            return BookSerializer
        if self.action == 'retrieve' or self.action == 'create':
            return SingleBookSerializer