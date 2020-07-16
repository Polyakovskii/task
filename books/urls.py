from django.urls import path
from .views import BookView
app_name = "books"

urlpatterns = [
    path('v1/books/', BookView.as_view({'get':'list', 'post':'create'})),
    path('v1/books/<int:pk>', BookView.as_view({'get': 'retrieve'}))
]