from django.contrib import admin
from apps.donation.models import ParticipantRegistration
from apps.donation.models import Participant
from apps.donation.models import Donation



@admin.register(ParticipantRegistration)
class ParticipantRegistrationAdmin(admin.ModelAdmin):

    list_display = (
        "get_first_name",
        "get_last_name",
        "get_email",
        "phone_number",
        "address",
        "registration_date",
    )

    search_fields = (
        "user__first_name",
        "user__last_name",
        "user__email",
    )

    list_filter = ("registration_date",)

    ordering = ("-registration_date",)

    # ambil data dari User
    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = "First Name"

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = "Last Name"

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = "Email"

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "total_donation",
        "total_transactions",
        "created_at",
    )

    search_fields = (
        "first_name",
        "last_name",
        "email",
        "phone_number",
    )

    list_filter = (
        "created_at",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "created_at",
    )


# ======================================================
# Donation
# ======================================================

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "participant",
        "amount",
        "status",
        "donated_at",
    )

    search_fields = (
        "participant__first_name",
        "participant__last_name",
        "participant__email",
        "stripe_payment_intent",
        "stripe_session_id",
    )

    list_filter = (
        "status",
        "donated_at",
    )

    ordering = (
        "-donated_at",
    )

    readonly_fields = (
        "stripe_session_id",
        "stripe_payment_intent",
        "donated_at",
    )