from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .filters import BookFilter
from .serializers import BookSerializer, SingleBookSerializer

class BookView(viewsets.GenericViewSet, viewsets.mixins.RetrieveModelMixin, viewsets.mixins.CreateModelMixin, viewsets.mixins.ListModelMixin):
    queryset = Book.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = BookFilter
    def get_serializer_class(self):
        if self.action == 'list':
            return BookSerializer
        if self.action == 'retrieve' or self.action == 'create':
            return SingleBookSerializer