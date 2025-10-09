from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking, name='booking'),
    path('book_appointment', views.book_appointment, name='book_appointment'),
    path('booking-submit', views.bookingSubmit, name='bookingSubmit'),
    path('user-panel', views.userPanel, name='userPanel'),
    path('user-update/<int:id>', views.userUpdate, name='userUpdate'),
    path('user-update-submit/<int:id>', views.userUpdateSubmit, name='userUpdateSubmit'),
    path('staff-panel', views.staffPanel, name='staffPanel'),
]
