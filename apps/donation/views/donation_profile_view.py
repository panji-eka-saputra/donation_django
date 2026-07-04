from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from apps.donation.serializers import DonationProfileSerializer


class DonationProfileView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        participant = request.user.participant

        serializer = DonationProfileSerializer(participant)

        return Response(serializer.data)