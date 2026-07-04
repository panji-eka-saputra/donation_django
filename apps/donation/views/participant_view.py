from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.donation.models import Participant
from apps.donation.serializers import ParticipantSerializer


class ParticipantView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        participant = Participant.objects.get(
            registration=request.user.participant
        )

        serializer = ParticipantSerializer(participant)

        return Response(serializer.data)