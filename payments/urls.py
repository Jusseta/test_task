from django.urls import path
from rest_framework.routers import DefaultRouter
from payments.apps import PaymentsConfig
from payments.views import PaymentViewSet, ItemDetailView

app_name = PaymentsConfig.name


router_payment = DefaultRouter()
router_payment.register(r'buy', PaymentViewSet, basename='payment')


urlpatterns = [
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
] + router_payment.urls
