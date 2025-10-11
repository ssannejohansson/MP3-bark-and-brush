from django.urls import path
from . import views
from .views import get_available_times, book_appointment

urlpatterns = [
    path('book/', views.book_appointment, name='book_appointment'),
    path('available-times/', get_available_times, name='available_times'),
]