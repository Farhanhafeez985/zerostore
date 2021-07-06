import os

from django.contrib import messages
from django.shortcuts import render, redirect

from Admin.models import Categories, Sub_Categories
from Order.models import Order_details
from Signup.models import User_model
from Vendors.models import Store, Products


# Create your views here.

def vendorpanel(request):
    v_id = request.session['obj_id']
    length_products = len(Products.objects.filter(store__user_id=v_id))
    orders = Order_details.objects.filter(store__user_id=v_id).count()
    context = {'length_products': length_products, 'orders': orders}
    return render(request, 'vendorpanel.html', context)


def create_store(request):
    if request.method == 'POST':
        postData = request.POST
        storeName = postData.get('storename')
        ntn = postData.get('ntn')
        image = request.FILES['image']
        v_id = postData.get('v_id')
        try:
            registerstore = Store(store_Name=storeName, ntn=ntn, store_image=image, user_id=v_id)
            registerstore.save()
            messages.success(request, 'store created')
            return redirect('store_info')
        except:
            messages.warning(request, 'You already Have a Store...!')
            return render(request, 'createstore.html')
    else:
        return render(request, 'createstore.html')


def store_info(request):
    data = Store.objects.filter(user_id=request.session['obj_id'])
    return render(request, 'viewstore.html', {'data': data})


def updatestore(request, id):
    str = Store.objects.get(pk=id)
    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(str.store_image) > 0:
                os.remove(str.store_image.path)
            str.store_image = request.FILES['image']
        str.store_Name = request.POST.get('storename')
        str.ntn = request.POST.get('ntn')
        str.user_id = request.POST.get('v_id')
        str.save()
        messages.success(request, 'Store update successfully')
        return redirect('store_info')
    else:
        return render(request, 'updatestore.html', {'str': str})


def deletestore(request, id):
    data = Store.objects.get(id=id)
    data.delete()
    messages.success(request, 'Store deleted successfully')
    return redirect('create_store')


def add_products(request):
    categories = Categories.objects.all()
    subcategories = Sub_Categories.objects.all()
    stores = Store.objects.all()
    context = {'categories': categories, 'subcategories': subcategories, 'stores': stores}

    if request.method == 'POST':
        try:
            postData = request.POST
            product_name = postData.get('proname')
            product_description = postData.get('prodescription')
            pic = request.FILES.get('proimage')
            ext = os.path.splitext(pic.name)[1]  # [0] returns path+filename
            valid_extensions = ['.jpg', '.png', '.jpeg']
            if not ext.lower() in valid_extensions:
                messages.success(request, 'Unsupported file or Corrupted image. ')
                return render(request, 'addvendorProducts.html', context)
            cat_id = postData.get('catid')
            subcat_id = postData.get('subcatid')
            quantity = postData.get('quantity')
            product_price = postData.get('proprice')
            try:
                val2 =int(product_price)
            except:
                messages.warning(request,'Please enter price correctly')
                return render(request,'addvendorProducts.html')
            discount_price = postData.get('discount')
            try:
                val = int(discount_price)
            except:
                messages.warning(request, 'Please enter price correctly')
                return render(request, 'addvendorProducts.html', context)
            data = Store.objects.get(user_id=request.session['obj_id'])
            Productdata = Products(product_name=product_name,
                                   product_price=val2,
                                   discount_price=val,
                                   product_description=product_description,
                                   product_image=pic,
                                   category_id=cat_id,
                                   subcategory_id=subcat_id,
                                   store_id=data.id, product_quantity=quantity)
            Productdata.save()
            messages.success(request, 'Product add successfully')
            return render(request, 'addvendorProducts.html', context)

        except:
            messages.info(request, 'Please create a Store First..')
            return redirect('create_store')

    else:
        return render(request, 'addvendorProducts.html', context)


def update_products(request, id):
    prod = Products.objects.get(id=id)
    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(prod.product_image) > 0:
                os.remove(prod.product_image.path)
            prod.product_image = request.FILES['proimage']
        prod.product_name = request.POST.get('proname')
        prod.product_price = request.POST.get('proprice')
        prod.discount_price = request.POST.get('discount')
        prod.product_description = request.POST.get('prodescription')
        prod.category_id = request.POST.get('catid')
        prod.subcategory_id = request.POST.get('subcatid')
        prod.product_quantity = request.POST.get('quantity')
        prod.save()

        return redirect('show_vendor_products')
    context = {'prod': prod}
    return render(request, 'update_vendor_pro.html', context)


def show_vendor_products(request):
    try:
        data = Store.objects.get(user_id=request.session['obj_id'])
        obj = Products.objects.filter(store_id=data)
        context = {'obj': obj}
        return render(request, 'showvendorproducts.html', context)
    except:
        messages.warning(request, 'You did not have any Products')
        return render(request, 'showvendorproducts.html')


def delete_products(request, id):
    data = Products.objects.filter(id=id)
    data.delete()
    return redirect('show_vendor_products')


def update_vendor_profile(request):
    try:
        data = User_model.objects.get(id=request.session['obj_id'])
        context = {'data': data}
        if request.method == "POST":
            if len(request.FILES) != 0:
                if len(data.image) > 0:
                    os.remove(data.image.path)
                data.image = request.FILES['image']
            data.fullname = request.POST.get('fullname')
            data.email = request.POST.get('email')
            data.password = request.POST.get('password1')
            data.confirm_password = request.POST.get('password2')
            if request.POST.get('password1') != request.POST.get('password2'):
                messages.warning(request, 'New Passwords not Match')
                return redirect('update_vendor_profile')
            else:
                data.save()
                messages.success(request, 'Profile Update..')
            return redirect('update_vendor_profile')
        else:
            return render(request, 'edit_vendor_profile.html', context)
    except:
        return render(request, 'edit_vendor_profile.html')


def total_orders(request):
    try:
        id = Store.objects.get(user_id=request.session['obj_id'])
        orders = Order_details.objects.filter(store_id=id)
        context = {'orders': orders}
        return render(request, 'vendor_orders.html', context)
    except:
        return render(request, 'vendor_orders.html')


def order_detail(request, id):
    order = Order_details.objects.get(id=id)
    if request.method == 'POST':
        order.status = request.POST.get('status')
        order.save()
        messages.success(request, 'update Successfully')
        return redirect('total_orders')
    return render(request, 'orderdetails.html', {'order': order})


def load_cat(request):
    cat_id = request.GET.get('catid')
    subcat = Sub_Categories.objects.filter(category_id=cat_id)
    return render(request, 'dropdownlist.html', {'subcat': subcat})
