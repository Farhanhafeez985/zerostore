import os

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect

from Customer.models import Customer_model, Wishlist, Comments
from Order.models import Order_details
# Create your views here.
from Vendors.models import Products


def customer_panel(request):
    try:
        customer_id = request.session['obj_id']
        orders = Order_details.objects.filter(order__customer_id=customer_id)
        context = {'orders': orders}
        return render(request, 'customer_panel.html', context)
    except:
        return render(request, 'customer_panel.html')


def profile_update(request):
    try:
        data = Customer_model.objects.get(id=request.session['obj_id'])
        if request.method == "POST":
            if len(request.FILES) != 0:
                if len(data.image) > 0:
                    os.remove(data.image.path)
                data.image = request.FILES['image']
            data.fullname = request.POST.get('fullname')
            data.email = request.POST.get('email')
            data.phone = request.POST.get('phone')
            data.password = request.POST.get('password1')
            data.confirm_password = request.POST.get('password2')
            if request.POST.get('password1') != request.POST.get('password2'):
                messages.warning(request, 'New Passwords not Match')
                return redirect('updateprofile')
            else:
                data.save()
                messages.success(request, 'Profile Update..')
            return redirect('updateprofile')
    except:
        messages.info(request, 'Please Create an accout')
        return render(request, 'customer_profile_update.html')
    else:
        return render(request, 'customer_profile_update.html', {'data': data})


def wish_list(request, id):
    url = request.META.get('HTTP_REFERER')
    try:
        data = Customer_model.objects.get(id=request.session['obj_id'])
        item_to_save = get_object_or_404(Products, pk=id)
        if Wishlist.objects.filter(user_id=data.id, item=id).exists():
            return redirect(url)
        user_list, created = Wishlist.objects.get_or_create(user_id=data.id)
        user_list.item.add(item_to_save)
        return redirect(url)
    except:
        return redirect('login')


def wished_product(request):
    try:
        user_id = request.session['obj_id']
        user_wishlist = Wishlist.objects.get(user_id=user_id).item.all()
        return render(request, 'wished_list.html', {'wp': user_wishlist})
    except:
        return render(request, 'wished_list.html')


def comment(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        msg = request.POST.get('message')
        u_id = request.session['obj_id']
        obj = Comments.objects.create(comment=msg, product_id=id, user_id=u_id)
        obj.save()
    return HttpResponseRedirect(url)


def delete_comment(request, id):
    url = request.META.get('HTTP_REFERER')
    cmnt = Comments.objects.get(id=id)
    cmnt.delete()
    return HttpResponseRedirect(url)

def delete_wish_pro(request,id):
    url = request.META.get('HTTP_REFERER')
    user_id = request.session['obj_id']
    Wishlist.objects.get(user_id=user_id).item.remove(Products.objects.get(id=id))
    return HttpResponseRedirect(url)