from rest_framework import serializers
from apps.donation.models import Participant


class ParticipantSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(
        source="registration.user.first_name",
        read_only=True
    )

    last_name = serializers.CharField(
        source="registration.user.last_name",
        read_only=True
    )

    email = serializers.EmailField(
        source="registration.user.email",
        read_only=True
    )

    class Meta:
        model = Participant

        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "total_donation",
            "total_transactions",
            "created_at",
        ]