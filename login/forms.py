from django import forms

from Signup.models import User_model, Customer_model


class UserloginForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your Email'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}), required=True)

    class Meta():
        model = User_model
        fields = ('fullname', 'password')


class CustomerloginForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your Email'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}), required=True)

    class Meta():
        model = Customer_model
        fields = ('fullname', 'password')