from django.contrib import admin
from apps.donation.models import ParticipantRegistration


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