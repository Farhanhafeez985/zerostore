from django.contrib import messages
from django.shortcuts import render,redirect

# Create your views here.
from Signup.forms import VendorSignupForm, CustomerSignupForm
from Signup.models import User_model, Customer_model


def signup(request):
    form2 = CustomerSignupForm()
    if request.method == 'POST' and 'form1' in request.POST:
        form = VendorSignupForm(request.POST, request.FILES)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            user_type = form.cleaned_data['user_type']
            pic = request.FILES['image']
            data = User_model.objects.create(fullname=fullname, email=email, password=password,
                                             confirm_password=confirm_password, user_type=user_type, image=pic)
            data.save()
            messages.success(request, 'Registration completed')
            return redirect('signup')
    else:
        form = VendorSignupForm()
        form2 = CustomerSignupForm()
    return render(request, 'register.html', {'form': form, 'form2': form2})


def customer_signup(request):
    form = VendorSignupForm()
    if request.method == 'POST' and 'form2' in request.POST:
        form2 = CustomerSignupForm(request.POST, request.FILES)
        if form2.is_valid():
            fullname = form2.cleaned_data['fullname']
            email = form2.cleaned_data['email']
            password = form2.cleaned_data['password']
            confirm_password = form2.cleaned_data['confirm_password']
            phone = form2.cleaned_data['phone']
            user_type = request.POST.get('customer')
            pic = request.FILES['image']
            data = Customer_model.objects.create(fullname=fullname, email=email, password=password,
                                                 confirm_password=confirm_password,
                                                 user_type=user_type, image=pic, phone=phone)
            data.save()
            messages.success(request, 'Registration completed')
            #return render(request, 'register.html', {'form': form, 'form2': form2})
            return redirect('customer_signup')
    else:
        form = VendorSignupForm()
        form2 = CustomerSignupForm()
    return render(request, 'register.html', {'form': form, 'form2': form2})
