from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponseRedirect

from Signup.forms import VendorSignupForm, CustomerSignupForm
from Signup.models import User_model, Customer_model


def loginview(request):
    form = VendorSignupForm()
    form2 = CustomerSignupForm()
    context = {'form': form, 'form2': form2}
    return_url = request.GET.get('next')
    if request.method == 'POST' and 'form1' in request.POST:
        postData = request.POST
        email = postData.get('email')
        pass1 = postData.get('password')
        try:
            obj = User_model.objects.get(email=email)
            if obj.password == pass1:
                if obj.user_type == 'vendor':
                    request.session['obj_id'] = obj.id
                    request.session['type'] = obj.user_type
                    request.session['fullname'] = obj.fullname
                    request.session['email'] = obj.email
                    if return_url:
                        return HttpResponseRedirect(return_url)
                    else:
                        return_url = None
                        return redirect('home')
                elif obj.user_type == 'seller':
                    request.session['obj_id'] = obj.id
                    request.session['type'] = obj.user_type
                    request.session['fullname'] = obj.fullname
                    request.session['email'] = obj.email
                    if return_url:
                        return HttpResponseRedirect(return_url)
                    else:
                        return_url = None
                        return redirect('home')
            else:
                messages.error(request, "Password Incorrect")
                return redirect('login')
        except:
            messages.warning(request, 'Email does not exist..!')
    if request.method == 'POST' and 'form2' in request.POST:
        postData = request.POST
        email = postData.get('email')
        pass1 = postData.get('password')
        try:
            obj = Customer_model.objects.get(email=email)
            if obj.password == pass1:
                request.session['obj_id'] = obj.id
                request.session['fullname'] = obj.fullname
                request.session['type'] = obj.user_type
                request.session['email'] = obj.email
                if return_url:
                    return HttpResponseRedirect(return_url)
                else:
                    return_url = None
                    return redirect('home')
            else:
                messages.error(request, 'Please Enter Correct Password')
                return redirect('login')
        except:
            messages.error(request, 'Email does not exist..!')

    return render(request, 'login.html', context)


def logout(request):
    request.session.flush()
    return redirect('home')
