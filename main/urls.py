from django.urls import path
from . import views
from .views import SuccessView, ContactView

urlpatterns = [
    # Static pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('gallery/', views.gallery, name='gallery'),

    # Booking and Login
    path('booking/', views.booking, name='booking'),
    path('book-login/', views.book_login, name="book-login"),

    # Contact modal
    path("contact/", ContactView.as_view(), name="contact"),
    path("success/", SuccessView.as_view(), name="success"),
]
