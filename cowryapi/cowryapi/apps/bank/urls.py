from django.urls import path
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import (BankView, BankCustomerJoinView,
                    ApproveCustomerView)


router = DefaultRouter()
router.register(r'banks', BankView, basename='banks')
# router.register()

urlpatterns = [
    path('banks/<int:bank_id>/join/', BankCustomerJoinView.as_view()),
    path('banks/<int:bank_id>/join/<int:pk>/', ApproveCustomerView.as_view())
]

urlpatterns += router.urls
