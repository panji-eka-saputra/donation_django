from rest_framework import serializers

from apps.donation.models import Donation


class PaymentSuccessSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(
        source="participant.first_name"
    )

    last_name = serializers.CharField(
        source="participant.last_name"
    )

    email = serializers.EmailField(
        source="participant.email"
    )

    class Meta:
        model = Donation

        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "amount",
            "status",
            "donated_at",
        ]