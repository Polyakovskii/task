from django.urls import path
from .views import BookView, SingleBookView
app_name = "books"

urlpatterns = [
    path('v1/books/', BookView.as_view()),
    path('v1/books/<int:pk>', SingleBookView.as_view())
]