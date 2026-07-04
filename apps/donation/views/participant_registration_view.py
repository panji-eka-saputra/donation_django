from apps.donation.models import ParticipantRegistration
from apps.donation.serializers import ParticipantRegistrationSerializer
from rest_framework.viewsets import ModelViewSet

class ParticipantRegistrationViewSet(ModelViewSet):
    queryset = ParticipantRegistration.objects.all()
    serializer_class = ParticipantRegistrationSerializer

    