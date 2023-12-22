from django.urls import path
from payments.apps import PaymentsConfig
from payments.views import StripeCheckoutView, ItemDetailView

app_name = PaymentsConfig.name


urlpatterns = [
    path('buy/<int:pk>/', StripeCheckoutView.as_view(), name='buy'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
]
