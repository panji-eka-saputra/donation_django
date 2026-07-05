from rest_framework import serializers
from apps.donation.models import Participant


class ParticipantProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participant
        fields = [
            "first_name",
            "last_name",
            "email",
            "birthdate",
            "phone_number",
            "address",
            "total_donation",
            "total_transactions",
        ]