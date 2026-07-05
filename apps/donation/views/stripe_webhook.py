import stripe

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from apps.donation.models import Donation

stripe.api_key = settings.STRIPE_SECRET_KEY


@csrf_exempt
def stripe_webhook(request):

    payload = request.body

    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")

    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

    try:

        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            endpoint_secret,
        )

    except ValueError:
        return HttpResponse(status=400)

    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)

    # ==========================
    # PAYMENT SUCCESS
    # ==========================

    if event["type"] == "checkout.session.completed":
        print("============== WEBHOOK ==============")


        session = event["data"]["object"]

        donation_id = session["metadata"]["donation_id"]

        donation = Donation.objects.get(
            id=donation_id
        )

        donation.status = Donation.Status.SUCCESS

        donation.stripe_payment_intent = session["payment_intent"]

        donation.save()

        participant = donation.participant

        participant.total_donation += donation.amount

        participant.total_transactions += 1

        participant.save()

        print("Donation Success :", donation.id)

    # ==========================
    # PAYMENT FAILED / EXPIRED
    # ==========================

    elif event["type"] == "checkout.session.expired":

        session = event["data"]["object"]

        donation_id = session["metadata"]["donation_id"]

        donation = Donation.objects.get(
            id=donation_id
        )

        donation.status = Donation.Status.FAILED

        donation.save()

        print("Donation Failed :", donation.id)

    return HttpResponse(status=200)