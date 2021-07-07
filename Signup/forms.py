from django import forms

from Signup.models import User_model, Customer_model
from django import forms

from Signup.models import User_model, Customer_model


class VendorSignupForm(forms.ModelForm):
    ALLOWED_TYPES = ['jpg', 'jpeg', 'png', 'gif']
    choice = ('-- Chose--',
              (
                  ('', '---chose--'),
                  ('vendor', 'Vendor'),
                  ('seller', 'Seller'),
              )),

    fullname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your Full Name'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your Email'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Type Alphanumeric password'}), required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Retype Alphanumeric password password'}),
                                       required=True)
    image = forms.ImageField(label='Select a file', required=True),
    user_type = forms.ChoiceField(required=True, choices=choice, widget=forms.Select(
        attrs={'class': 'form-control , form-control-alternative', 'text-align':
            'center', '-ms-text-align-last': 'center',
               '-moz-text-align-last': 'center',
               'text-align-last': 'center', }))

    class Meta():
        model = User_model
        fields = ('fullname', 'email', 'password', 'confirm_password', 'image', 'user_type')

    def clean_fullname(self):
        user = self.cleaned_data['fullname']
        try:
            match = User_model.objects.get(fullname=user)
        except:
            return self.cleaned_data['fullname']
        raise forms.ValidationError("This username is already Exist")

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            match = User_model.objects.get(email=email)
        except:
            return self.cleaned_data['email']
        raise forms.ValidationError("This Email is already Exist")

    def clean_confirm_password(self):
        pas = self.cleaned_data['password']
        cpass = self.cleaned_data['confirm_password']
        # MIN_LENGTH = 8
        if pas and cpass:
            if pas != cpass:
                raise forms.ValidationError("Password and Confirm Password Not Match")
            else:
                if pas.isdigit():
                    raise forms.ValidationError("Password is not all numaric")
        return cpass

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            raise forms.ValidationError('Missing image file')
        return image


class CustomerSignupForm(forms.ModelForm):
    fullname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your Full Name'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your Email'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Type Alphanumeric password', 'id': 'id_pass'}),
                               required=True, min_length=8, max_length=20)
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Retype Alphanumeric password', 'id': 'id_con_pass'}), min_length=8,
        max_length=20,
        required=True)
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter you phone Number'}), required=True)
    image = forms.ImageField(),

    class Meta():
        model = Customer_model
        fields = ('fullname', 'email', 'password', 'confirm_password', 'image', 'phone')

    def clean_fullname(self):
        user = self.cleaned_data['fullname']
        try:
            match = Customer_model.objects.get(fullname=user)
        except:
            return self.cleaned_data['fullname']
        raise forms.ValidationError("This username is already Exist")

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            match = Customer_model.objects.get(email=email)
        except:
            return self.cleaned_data['email']
        raise forms.ValidationError("This Email is already Exist")

    def clean_confirm_password(self):
        pas = self.cleaned_data['password']
        cpass = self.cleaned_data['confirm_password']
        # MIN_LENGTH = 8
        if pas and cpass:
            if pas != cpass:
                raise forms.ValidationError("Password and Confirm Password Not Match")
            else:
                if pas.isdigit():
                    raise forms.ValidationError("Password is not all numaric")
        return cpass

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            raise forms.ValidationError('Missing image file')
        return image