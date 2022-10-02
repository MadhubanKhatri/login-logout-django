from django.urls import path
from .views import Home, LoginView, LogoutView, RegisterView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]