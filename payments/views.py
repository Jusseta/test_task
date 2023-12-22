from django.conf import settings
import stripe
from django.views.generic import DetailView
from rest_framework.response import Response
from rest_framework import viewsets, status
from payments.models import Item
from payments.serializers import ItemSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def retrieve(self, request, *args, **kwargs):
        stripe.api_key = settings.STRIPE_KEY

        session = stripe.checkout.Session.create(
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {"name": request.data.get('name')},
                        "unit_amount": request.data.get('price'),
                    },
                    "quantity": 1,
                },
            ],
            mode="payment",
            success_url=settings.DOMAIN_URL + f'/cart/item/{request.data.get("id")}',
        )

        return Response({session.id}, status=status.HTTP_200_OK)


class ItemDetailView(DetailView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data
