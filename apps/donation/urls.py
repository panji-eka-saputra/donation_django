from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.donation.views import (
    ParticipantRegistrationViewSet,
    ParticipantProfileView, DonationProfileView
)

from apps.donation.views.stripe_webhook import stripe_webhook

urlpatterns = [

    # Stripe
    path(
        "webhook/",
        stripe_webhook,
        name="stripe-webhook"
    ),

    # Registration
    path(
        "participant-registrations/",
        ParticipantRegistrationViewSet.as_view({
            "get": "list",
            "post": "create",
        }),
        name="participant-registration-list",
    ),

    path(
        "participant-registrations/<int:pk>/",
        ParticipantRegistrationViewSet.as_view({
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy",
        }),
        name="participant-registration-detail",
    ),

    # Logged-in participant profile
    path(
        "participant/me/",
        ParticipantProfileView.as_view(),
        name="participant-profile",
    ),
    path(
        "donation/me/",
        DonationProfileView.as_view(),
        name="donation-profile",
    ),

    # Authentication
    path(
        "token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),

    path(
        "token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
]