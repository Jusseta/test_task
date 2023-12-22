from django.urls import path
from rest_framework.routers import DefaultRouter
from payments.apps import PaymentsConfig
from payments.views import PaymentViewSet, ItemDetailView

app_name = PaymentsConfig.name


urlpatterns = [
    path('buy/<int:pk>/', PaymentViewSet.as_view({'get': 'retrieve'}), name='buy'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
]
