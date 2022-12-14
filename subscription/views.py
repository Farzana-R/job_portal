import stripe

from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.shortcuts import render, redirect

from . models import Customer, CustomerStatus

stripe.api_key = settings.STRIPE_SECRET_KEY

def special(request):
    return render(request, 'membership/specials.html')


# def premium(request):
#     return render(request, 'membership/premium.html')


@login_required
def settings(request):
    membership = False
    cancel_at_period_end = False
    if request.method == 'POST':
        subscription = stripe.Subscription.retrieve(
            request.user.customer.stripe_subscription_id)
        subscription.cancel_at_period_end = True
        request.user.customer.cancel_at_period_end = True
        cancel_at_period_end = True
        subscription.save()
        request.user.customer.save()
    else:
        try:
            if request.user.customer.membership:
                membership = True
                subscription = stripe.Subscription.retrieve(
                    request.user.customer.stripe_subscription_id)
                product = stripe.Product.retrieve(subscription.plan.product)
            if request.user.customer.cancel_at_period_end:
                cancel_at_period_end = True
        except Customer.DoesNotExist:
            membership = False

    return render(request, 'membership/home.html',
                  {'membership': membership,
                   'cancel_at_period_end': cancel_at_period_end})


@user_passes_test(lambda u: u.is_superuser)
def updateaccounts(request):
    customers = Customer.objects.all()
    for customer in customers:
        subscription = stripe.Subscription.retrieve(
            customer.stripe_subscription_id)
        if subscription.status != 'active':
            customer.membership = False
        else:
            customer.membership = True
        customer.cancel_at_period_end = subscription.cancel_at_period_end
        customer.save()
    return render(request, 'home.html', {'customers': customers})


def join(request):
    return render(request, 'subscription/home.html')


def success(request):
    if request.method == 'GET' and 'session_id' in request.GET:
        session = stripe.checkout.Session.retrieve(request.GET['session_id'], )
        customer = Customer()
        customer = Customer.objects.get(user=request.user)
        customer.stripeid = session.customer
        customer.membership = True
        customer.cancel_at_period_end = False
        customer.stripe_subscription_id = session.subscription
        CustomerStatus.status = 'active'

        customer.save()
        subscription = stripe.Subscription.retrieve(
            customer.stripe_subscription_id)
        product = stripe.Product.retrieve(subscription.plan.product)
    return render(request, 'membership/home.html', {'subscription': subscription, 'product': product})


def cancel(request):
    return render(request, 'membership/cancel.html')


@login_required
def checkout(request):
    try:
        if request.user.customer.membership:
            return redirect('subscription:settings')
    except Customer.DoesNotExist:
        pass

    if request.method == 'POST':
        pass
    else:
        membership = 'daily'
        final_price = 5
        price_id = 'price_1MEZ4VSDMbDGBwOWozb7A8pH'
        if request.method == 'GET' and 'membership' in request.GET:
            if request.GET['membership'] == 'monthly':
                membership = 'monthly'
                price_id = 'price_1ME3zNSDMbDGBwOWuztjwtuE'
                final_price = 50

            elif request.GET['membership'] == 'yearly':
                membership = 'yearly'
                price_id = 'price_1ME3zNSDMbDGBwOW6Tz3qLB6'
                final_price = 500

        # Create Stripe Checkout
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            customer_email=request.user.email,
            line_items=[{
                'price': price_id,
                'quantity': 1,
            }],
            mode='subscription',
            allow_promotion_codes=True,
            success_url='http://127.0.0.1:8000/subscription_appsuccess?session_id={CHECKOUT_SESSION_ID}',
            cancel_url='http://127.0.0.1:8000/cancel',
        )

        return render(request, 'subscription/checkout.html', {'final_price': final_price, \
        'session_id': session.id, 'membership': membership})


def pausesubscription(request):
    cid = stripe.Subscription.retrieve(
        request.user.customer.stripe_subscription_id),
    stripe.Subscription.modify(
        request.user.customer.stripe_subscription_id,
        pause_collection={
            'behavior': 'mark_uncollectible',
        },
    )
    Customer.status = 'pause'
    return render(request, 'membership/home.html')


def resumesubscription(request):
    cid = stripe.Subscription.retrieve(
        request.user.customer.stripe_subscription_id),
    stripe.Subscription.modify(
        request.user.customer.stripe_subscription_id,
        pause_collection='',
    )
    Customer.status = 'active'
    return render(request, 'membership/home.html')


def updatesubscription(request):
    if request.method == 'GET':
        current_subscription = stripe.Subscription.retrieve(request.user.customer.stripe_subscription_id)
        # new plan
        stripe.Subscription.modify(
            current_subscription.id,
            cancel_at_period_end=False,
            proration_behavior='create_prorations',

            # the new subscription
            items=[{
                'id': current_subscription['items']['data'][0].id,
                'price': 'price_1ME3zNSDMbDGBwOW6Tz3qLB6',
            },
            ]
        )

        return render(request, 'membership/home.html')

def Deletesubscription(request):
    stripe.Subscription.delete(stripe.Subscription.retrieve(request.user.customer.stripe_subscription_id)),
    Customer.objects.get(user=request.user).delete()
    Customer.objects.create(user=request.user)

    return redirect('/deletemsg')