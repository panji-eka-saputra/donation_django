import stripe
from decimal import Decimal

from django.conf import settings

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from apps.donation.models import (
    Participant,
    Donation,
)

stripe.api_key = settings.STRIPE_SECRET_KEY


class DonationView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        amount = request.data.get("amount")

        if not amount:
            return Response(
                {
                    "message": "Donation amount is required."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        participant = Participant.objects.get(
            registration__user=request.user
        )

        donation = Donation.objects.create(
            participant=participant,
            amount=Decimal(amount),
            status=Donation.Status.PENDING
        )

        checkout_session = stripe.checkout.Session.create(

            payment_method_types=["card"],

            mode="payment",

            customer_email=participant.email,

            line_items=[
                {
                    "price_data": {
                        "currency": "idr",
                        "product_data": {
                            "name": "Donation",
                        },
                        "unit_amount": int(Decimal(amount) * 100),
                    },
                    "quantity": 1,
                }
            ],

            metadata={
                "donation_id": donation.id,
            },

            success_url="http://localhost:5173/payment-success",

            cancel_url="http://localhost:5173/payment-cancel",
        )

        donation.stripe_session_id = checkout_session.id
        donation.save()

        return Response(
            {
                "checkout_url": checkout_session.url
            },
            status=status.HTTP_200_OK
        )