from django.urls import path
from .views import signup, EmailLoginView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', EmailLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('account/', views.my_account, name='my_account'),
]
