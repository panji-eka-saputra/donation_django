from rest_framework import serializers
from apps.donation.models import Participant

class DonationProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(source="user.email")

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