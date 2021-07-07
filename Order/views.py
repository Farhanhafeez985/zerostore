from random import randint
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from Order.models import Order, Order_details
from Vendors.models import Products

# Create your views here.

def checkout(request):
    if request.method == "POST":
        address = request.POST.get('address')
        city = request.POST.get('city')
        postcode = request.POST.get('postcode')
        phone = request.POST.get('phone')
        totalprice = request.POST.get('total')
        cart = request.session.get('cart')
        rannum = randint(100000000000, 199999999999)
        products = Products.get_product_by_id(list(cart.keys()))
        if products:
            orders = Order(customer_id=request.session['obj_id'],
                           address=address,
                           city=city,
                           total_price=totalprice,
                           postcode=postcode,
                           phone=phone,
                           Order_id=rannum
                           )
            orders.placeorder();
            last_order = Order.objects.last()
            oid = last_order.id
            for product in products:
                detail = Order_details(quantity= cart.get(str(product.id)),
                                       price=product.product_price,
                                       order_id=oid,
                                       product_id=product.id,
                                       status='none',
                                       store_id=product.store_id)
                detail.save()
            messages.success(request, 'Order Placed Successfully')
            request.session['cart'] = {}
            return render(request, 'checkout.html')
        else:
            messages.info(request,'Please chose atleast one product.')
            return  redirect('checkout')
    else:
        cart = request.session.get('cart')
        products = Products.get_product_by_id(list(cart.keys()))
        return render(request, 'checkout.html', {'check_products': products})
