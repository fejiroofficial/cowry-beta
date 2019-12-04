from django.urls import path
from rest_framework.authtoken import views
from .views import UserCreateView

urlpatterns = [
    path('auth/register/', UserCreateView.as_view(), name='user_signup'),
    path('auth/login/', views.obtain_auth_token, name='login')
]