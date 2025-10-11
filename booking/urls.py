from django.urls import path
from . import views
from .views import get_available_times, book_appointment
from .views import get_fully_booked_dates, update_appointment
from .views import my_appointments


urlpatterns = [
    path('available-times/', get_available_times, name='available_times'),
    path('fully-booked-dates/', get_fully_booked_dates, name='fully_booked_dates'),
    path('book/', book_appointment, name='book_appointment'),
    path('success/', views.appointment_success, name='appointment_success'), 
    path('appointment/<int:pk>/update/', update_appointment, name='update_appointment'),
    path('my-appointments/', my_appointments, name='my_appointments'),
]