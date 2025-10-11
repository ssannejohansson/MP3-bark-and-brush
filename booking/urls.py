from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_appointment, name='book_appointment'),
    path('available-times/', views.get_available_times, name='available_times'),
]