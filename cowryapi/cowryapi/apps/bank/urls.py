from django.urls import path
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import (BankView, BankCustomerJoinView,
                    ApproveRetrieveCustomerView, PaymentView)


router = DefaultRouter()
router.register(r'banks', BankView, basename='banks')

urlpatterns = [
    path('banks/<int:bank_id>/join/', BankCustomerJoinView.as_view()),
    path('banks/<int:bank_id>/customers/<int:pk>/', ApproveRetrieveCustomerView.as_view()),
    path('banks/<int:bank_id>/customers/<int:pk>/payment/', PaymentView.as_view())
]

urlpatterns += router.urls
