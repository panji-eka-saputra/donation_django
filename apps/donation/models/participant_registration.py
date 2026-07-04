from django.db import models
from django.contrib.auth.models import User

class ParticipantRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="participant_registration")

    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)
    # email = models.EmailField(unique=True)
    birthdate = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    is_agree_to_terms = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"