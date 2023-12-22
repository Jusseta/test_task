from django.conf import settings
import stripe
from django.shortcuts import redirect
from django.views.generic import DetailView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from payments.models import Item
from payments.serializers import ItemSerializer


class StripeCheckoutView(APIView):
    """Creating a stripe checkout session"""

    def get(self, request, pk):
        item = Item.objects.get(id=pk)
        stripe.api_key = settings.STRIPE_KEY
        try:
            session = stripe.checkout.Session.create(
                line_items=[
                    {
                        "price_data": {
                            "currency": "rub",
                            "unit_amount": item.price,
                            "product_data": {"name": item.name},
                        },
                        "quantity": 1,
                    },
                ],
                mode="payment",
                success_url=settings.DOMAIN_URL + f'/cart/item/{item.pk}',
            )
            return redirect(session.url)

        except:
            return Response(
                {'Something went wrong when creating stripe checkout session'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ItemDetailView(DetailView):
    """Detailed item page"""
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data
