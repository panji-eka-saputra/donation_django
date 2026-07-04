from rest_framework import serializers
from apps.donation.models import (ParticipantRegistration, Participant)
from datetime import date
from django.contrib.auth.models import User

class ParticipantRegistrationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    class Meta:
        model = ParticipantRegistration
        fields = ['first_name', 'last_name', 'email', 'password', 'phone_number', 'address', 'registration_date', 'is_agree_to_terms', 'birthdate']
        extra_kwargs = {
            "first_name": {
                "required": True,
                "error_messages": {
                    "required": "First Name is required.",
                    "blank": "First Name cannot be empty."
                }
            },
            "last_name": {
                "required": True,
                "error_messages": {
                    "required": "Last Name is required.",
                    "blank": "Last Name cannot be empty."
                }
            },
            "email": {
                "required": True,
                "error_messages": {
                    "required": "Email is required.",
                    "blank": "Email cannot be empty."
                }
            },
            "birthdate": {
                "required": True,
                "error_messages": {
                    "required": "Birthdate is required.",
                    "blank": "Birthdate cannot be empty."
                }
            },
            "is_agree_to_terms": {
                "required": True,
                "error_messages": {
                    "required": "You must agree to the terms and conditions.",
                }
            }
        }

    def validate_birth_date(self, value):
        """
        Validate participant age.
        Minimum age is 18 years old.
        """

        today = date.today()

        age = (
            today.year
            - value.year
            - ((today.month, today.day) < (value.month, value.day))
        )

        if age < 18:
            raise serializers.ValidationError(
                "Participant must be at least 18 years old."
            )

        return value
    
    def validate_email(self, value):

        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "Email already exists."
            )

        return value

    def create(self, validated_data):

        first_name = validated_data.pop("first_name")
        last_name = validated_data.pop("last_name")
        email = validated_data.pop("email")
        password = validated_data.pop("password")

        birthdate = validated_data.get("birthdate")
        phone_number = validated_data.get("phone_number")
        address = validated_data.get("address")

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        participant_registration = ParticipantRegistration.objects.create(
            user=user,
            birthdate=birthdate,
            phone_number=phone_number,
            address=address,
            is_agree_to_terms=validated_data.get("is_agree_to_terms"),
        )

        Participant.objects.create(
            registration=participant_registration,
            first_name=first_name,
            last_name=last_name,
            email=email,
            birthdate=birthdate,
            phone_number=phone_number,
            address=address,
        )

        return participant_registration