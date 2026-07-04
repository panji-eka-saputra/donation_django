from django.db import models
from .participant import Participant

class Donation(models.Model):

    class Status(models.TextChoices):

        PENDING = "PENDING", "Pending"

        SUCCESS = "SUCCESS", "Success"

        FAILED = "FAILED", "Failed"


    participant = models.ForeignKey(
        Participant,
        on_delete=models.CASCADE,
        related_name="donations"
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    stripe_session_id = models.CharField(
        max_length=255,
        blank=True
    )

    stripe_payment_intent = models.CharField(
        max_length=255,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    donated_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        db_table = "donation"

    def __str__(self):
        return f"{self.participant} - {self.amount}"