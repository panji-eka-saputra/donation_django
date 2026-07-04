from rest_framework import serializers
from apps.donation.models import ParticipantRegistration
from django.contrib.auth.models import User

class ParticipantProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantRegistration
        fields = ["first_name",
            "last_name",
            "email",
            "birthdate",
            "phone_number",
            "address",]
        
        def update(self, instance, validated_data):
            user_data = validated_data.pop("user", {})

            user = instance.user

            user.first_name = user_data.get("first_name", user.first_name)
            user.last_name = user_data.get("last_name", user.last_name)
            user.email = user_data.get("email", user.email)

            user.save()

            instance.birthdate = validated_data.get(
                "birthdate",
                instance.birthdate
            )

            instance.phone_number = validated_data.get(
                "phone_number",
                instance.phone_number
            )

            instance.address = validated_data.get(
                "address",
                instance.address
            )

            instance.save()

            return instance