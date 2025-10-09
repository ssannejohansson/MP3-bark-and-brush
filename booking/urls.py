from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking, name='booking'),
    path('booking', views.booking, name='booking'),
    path('booking-submit', views.bookingSubmit, name='bookingSubmit'),
]
