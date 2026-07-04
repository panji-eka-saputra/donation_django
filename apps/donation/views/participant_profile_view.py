from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from apps.donation.models import ParticipantRegistration
from apps.donation.serializers import ParticipantProfileSerializer


class ParticipantProfileView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        registration = ParticipantRegistration.objects.get(
            user=request.user
        )

        participant = registration.participant

        serializer = ParticipantProfileSerializer(participant)

        return Response(serializer.data)

    def put(self, request):

        registration = ParticipantRegistration.objects.get(
            user=request.user
        )

        participant = registration.participant

        serializer = ParticipantProfileSerializer(
            participant,
            data=request.data,
            partial=True
        )

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)