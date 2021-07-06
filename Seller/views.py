import os

from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from Admin.models import Categories, Sub_Categories
from Seller.forms import Ad_Post_Form
from Seller.models import Used_Products
from Signup.models import User_model


def sellerpanel(request):
    count = len(Used_Products.objects.filter(user_id=request.session['obj_id']))
    ads = Used_Products.objects.filter(user_id=request.session['obj_id'])
    context = {'count': count, 'ads': ads}
    return render(request, 'sellerpanel.html', context)


def edit_profile(request):
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
            return redirect('edit_profile')
        else:
            data.save()
            messages.success(request, 'Profile Updated..')
        return redirect('edit_profile')
    else:
        return render(request, 'edit_seller_profile.html', context)


def ad_post(request):
    form = Ad_Post_Form(request.POST)
    categories = Categories.objects.all()
    subcategories = Sub_Categories.objects.all()
    context = {'categories': categories, 'subcategories': subcategories, 'form': form}

    if request.method == 'POST' and request.FILES:
        title = request.POST.get('ad_title')
        desc = request.POST.get('ad_description')
        cat_id = request.POST.get('catid')
        subcat_id = request.POST.get('subcatid')
        user_id = request.POST.get('userid')
        condition = request.POST.get('ad_condition')
        location = request.POST.get('ad_location')
        phone = request.POST.get('ad_phone')
        image = request.FILES.get('ad_image')
        ext = os.path.splitext(image.name)[1]  # [0] returns path+filename
        valid_extensions = ['.jpg', '.png', '.jpeg']
        if not ext.lower() in valid_extensions:
            messages.success(request, 'Unsupported file or Corrupted image. ')
            return render(request, 'postad.html', context)
        else:
            price = request.POST.get('ad_price')
            try:
                val = int(price)
                data = Used_Products.objects.create(ad_title=title, ad_price=val,
                                                    ad_description=desc, ad_condition=condition,
                                                    ad_location=location, ad_image=image,
                                                    category_id=cat_id, subcategory_id=subcat_id, user_id=user_id,
                                                    ad_phone=phone)
                data.save()
                messages.success(request, 'Ad Post Successfully')
                return redirect('ad_post')
            except:
                messages.warning(request, 'Please enter price correctly')
                return render(request, 'postad.html', context)
    else:
        return render(request, 'postad.html', context)


def your_ads(request):
    data = Used_Products.objects.filter(user_id=request.session['obj_id'])
    if data.exists():
        return render(request, 'sellerProducts.html', {'data': data})
    else:
        messages.info(request, 'You did not have Any ad..!')
        return render(request, 'sellerProducts.html')


def delete_ad(request, id):
    data = Used_Products.objects.filter(id=id)
    data.delete()
    return redirect('your_ads')


def edit_ad(request, id):
    categories = Categories.objects.all()
    subcategories = Sub_Categories.objects.all()
    ad = Used_Products.objects.get(id=id)
    context = {'category': categories, 'subcategory': subcategories, 'ad': ad}
    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(ad.ad_image) > 0:
                os.remove(ad.ad_image.path)
            ad.ad_image = request.FILES['image']
        ad.ad_title = request.POST.get('ad_title')
        ad.ad_description = request.POST.get('ad_description')
        ad.category_id = request.POST.get('catid')
        ad.subcategory_id = request.POST.get('subcatid')
        ad.user_id = request.POST.get('userid')
        ad.ad_condition = request.POST.get('ad_condition')
        ad.ad_location = request.POST.get('ad_location')
        ad.ad_phone = request.POST.get('ad_phone')
        price = request.POST.get('ad_price')
        try:
            val = int(price)
            ad.ad_price = val
            ad.save()
            messages.success(request, 'Ad update successfully')
            return redirect('your_ads')
        except:
            messages.warning(request, 'Please enter price correctly')
            return render(request, 'edit_seller_ad.html', context)
    return render(request, 'edit_seller_ad.html', context)
