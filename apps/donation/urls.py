# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from apps.donation.views import (ParticipantRegistrationViewSet, ParticipantProfileView)
# from apps.donation.views.stripe_webhook import stripe_webhook
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

# # the code below is if you want to use url default router for the viewset.
# # router = DefaultRouter()
# # router.register(r'participant-registrations', ParticipantRegistrationViewSet, basename='participant-registration')
# # urlpatterns = [
# #     path('', include(router.urls)),
# # ]

# urlpatterns = [
#     #for stripe
#     path("webhook/", stripe_webhook),
#     #Registration Purpose
#     path(
#         'participant-registrations/',
#         ParticipantRegistrationViewSet.as_view({
#             'get': 'list',
#             'post': 'create',
#         }),
#         name='participant-registration-list'
#     ),

#     path(
#         'participant-registrations/<int:pk>/',
#         ParticipantRegistrationViewSet.as_view({
#             'get': 'retrieve',
#             'put': 'update',
#             'patch': 'partial_update',
#             'delete': 'destroy',
#         }),
#         name='participant-registration-detail'
#     ),
#     path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
#     path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
# ]

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.donation.views import (
    ParticipantRegistrationViewSet,
    ParticipantProfileView,
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