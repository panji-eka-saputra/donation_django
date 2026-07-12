import stripe

from django.conf import settings

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from apps.donation.models import Donation
from apps.donation.serializers import PaymentSuccessSerializer

stripe.api_key = settings.STRIPE_SECRET_KEY


class PaymentSuccessView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        session_id = request.GET.get("session_id")

        if not session_id:

            return Response(
                {
                    "message": "session_id is required."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        session = stripe.checkout.Session.retrieve(
            session_id
        )

        donation = Donation.objects.get(
            stripe_session_id=session.id
        )

        serializer = PaymentSuccessSerializer(
            donation
        )

        return Response(serializer.data)