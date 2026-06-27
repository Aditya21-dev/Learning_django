from django.shortcuts import render, redirect
from .models import Product , Order_Payment
from django.forms.models import model_to_dict
import razorpay

def landing(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")

        Product.objects.create(
            name=name,
            price=price
        )

        return redirect('payment')  # reload page

    return render(request, 'landing.html')


def payment(request):
    products = Product.objects.all()
    total = sum(p.price for p in products)

    return render(request, 'payment.html', {
        'products': products,
        'total': total
    })



def razerpay(request):
    if request.method == 'POST':

        products = Product.objects.all()
        total = sum(p.price for p in products)
        amount = total * 100  # paise

        client = razorpay.Client(auth=("rzp_test_pr99iascS1WRtU", "UTDIzPGwICnAssu3Q3lk7zUi"))

        order = client.order.create({
            "amount": amount,
            "currency": "INR",
            "receipt": "order_rcptid_11"
        })

        # DB me save
        Order_Payment.objects.create(
            order_id=order['id'],
            amount=amount
        )

        # same page pe wapas bhejo + order ke sath
        return render(request, 'payment.html', {
            'products': products,
            'total': total,
            'order': order
        })
    

