from django.contrib import messages
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from Admin.models import admin_tbl, Categories, Sub_Categories
from Order.models import Order_details, Order
# Create your views here.
from Seller.models import Used_Products
from Signup.models import User_model, Customer_model
from Vendors.models import Products


def adminlogin(request):
    return_url = request.GET.get('next')
    if request.method == 'POST':
        postData = request.POST
        username = postData.get('username')
        password = postData.get('password')
        try:
            obj = admin_tbl.objects.get(username=username)
            if obj.password == password:
                request.session['obj_id'] = obj.id
                request.session['username'] = obj.username
                if return_url:
                    return HttpResponseRedirect(return_url)
                else:
                    return_url = None
                    return redirect('adminpanel')
            else:
                messages.error(request, 'Password incorrect.. ')
                return render(request,'admin.html')
        except:
            messages.error(request,'Username Not Exist ')
            return render(request, 'admin.html')
    else:
        return render(request,'admin.html')


def Adminpanel(request):
    try:
        total_order_prices = Order.objects.aggregate(Sum('total_price'))
        totalAmonut = total_order_prices['total_price__sum']
        total_Used_products = len(Used_Products.objects.all())
        total_new_products = len(Products.objects.all())
        total_order = len(Order.objects.all())
        context = {'total_order_prices': totalAmonut,
                   'total_Used_products': total_Used_products,
                   'total_new_products': total_new_products,
                   'total_order': total_order}
        return render(request, 'adminpanel.html', context)
    except:
        return render(request, 'adminpanel.html')


def addcat(request):
    try:
        if request.method == 'POST':
            categories = Categories.objects.all()
            context = {'categories': categories}
            postData = request.POST
            cat_name = postData.get('catname')
            admin_id =request.session['obj_id']
            catdata = Categories(Cat_name=cat_name,admin_id=admin_id)
            catdata.save()
            messages.success(request, "Category addded...!")
            return render(request, 'categories.html', context)
        else:
            categories = Categories.objects.all()
            context = {'categories': categories}
        return render(request, 'categories.html', context)
    except:
        messages.warning(request, 'Something is wrong...!')
        categories = Categories.objects.all()
        context = {'categories': categories}
    return render(request, 'categories.html', context)


def addsubcat(request):
    if request.method == 'POST':
        categories = Categories.objects.all()
        subcategories = Sub_Categories.objects.all()
        context = {'categories': categories, 'subcategories': subcategories}
        postData = request.POST
        subcat_name = postData.get('subcatname')
        catid = postData.get('catid')
        if catid:
            subcatdata = Sub_Categories(subcat_name=subcat_name, category_id=catid)
            subcatdata.save()
            messages.success(request, "Sub Category addded...!")
            return render(request, 'categories.html', context)
        else:
            messages.info(request, 'Please chose parent Category')
            return redirect('addsubcat')
    else:
        categories = Categories.objects.all()
        subcategories = Sub_Categories.objects.all()
        context = {'categories': categories, 'subcategories': subcategories}
        return render(request, 'categories.html', context)


def edit_cat(request, id):
    data = Categories.objects.get(id=id)
    context = {'data': data}
    if request.method == 'POST':
        catname = request.POST.get('catname')
        data.Cat_name=catname
        data.save()
        return redirect('catdata')
    return render(request, 'editcat.html', context)


def edit_Subcat(request, id):
    data =Sub_Categories.objects.get(id=id)
    context = {'data': data}
    if request.method == 'POST':
        subcat_name = request.POST.get('subcatname')
        data.subcat_name = subcat_name
        data.save()
        return redirect('subcatdata')
    return render(request, 'edit_subcat.html',context)


def catdata(request):
    if request.method == 'GET':
        categories = Categories.objects.all()
        context = {'categories': categories}
        return render(request, 'catlist.html', context)


def subcatdata(request):
    if request.method == 'GET':
        subcategories = Sub_Categories.objects.all()
        context = {'subcategories': subcategories}
        return render(request, 'subcatlist.html', context)


def deletecat(request, id):
    if request.method == 'POST':
        data = Categories.objects.get(pk=id)
        data.delete()
        return redirect('catdata')


def deletesubcat(request, id):
    if request.method == 'POST':
        data = Sub_Categories.objects.get(pk=id)
        data.delete()
        return redirect('subcatdata')


def show_order(request):
    orders = Order.objects.all()
    order_product = Order_details.objects.values('status')
    return render(request, 'orderslist.html', {'orders': orders, 'order_products': order_product})


# Products relate

def show_oldpro(request):
    return render(request, 'oldproducts.html')


def show_newpro(request):
    return render(request, 'newproducts.html')


# Vendors Stores related
def show_vendors_store(request):
    return render(request, 'vendorstore.html')


# vendor and seller Data
def showuserdata(request):
    return render(request, 'vendor_info.html')


def customerinfo(request):
    return render(request, 'customer_info.html')


# delete user
def deleteusers(request, id):
    data = User_model.objects.get(pk=id)
    data.delete()
    return redirect('showuserdata')



def deletecustomer(request, id):
    customer = Customer_model.objects.get(id=id)
    customer.delete()
    return redirect('customerinfo')


def adminlogout(request):
    request.session.flush()
    return redirect('admin')

def del_new_pro(request, id):
    data = Products.objects.get(pk=id)
    data.delete()
    return redirect('newproduct')

def del_old_pro(request, id):
    data = Used_Products.objects.get(pk=id)
    data.delete()
    return redirect('oldproduct')