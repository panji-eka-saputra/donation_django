from django.db import models
from .participant_registration import ParticipantRegistration

class Participant(models.Model):

    registration = models.OneToOneField(
        ParticipantRegistration,
        on_delete=models.CASCADE,
        related_name="participant"
    )

    first_name = models.CharField(
        max_length=30
    )

    last_name = models.CharField(
        max_length=30
    )

    email = models.EmailField(
        unique=True
    )

    birthdate = models.DateField(
        blank=True,
        null=True
    )

    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    address = models.TextField(
        blank=True,
        null=True
    )

    total_donation = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    total_transactions = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        db_table = "participant"

    def __str__(self):
        return self.first_name + " " + self.last_name