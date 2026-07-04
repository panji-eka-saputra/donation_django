from django.http import HttpResponse

def stripe_webhook(request):
    print("Webhook success Stripe")
    return HttpResponse(status=200)