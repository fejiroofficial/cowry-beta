from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BankView


router = DefaultRouter()
router.register(r'banks', BankView, basename='banks')
urlpatterns = router.urls
