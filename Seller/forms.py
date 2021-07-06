from django import forms

from Seller.models import Used_Products

choice = ('-- Chose--',
          (
              ('new', 'NEW'),
              ('USED', 'USED'),
          )),
locations = ('-- Chose--',
             (
                 ('gujrat', 'GUJRAT'),
                 ('lahore', 'LAHORE'),
                 ('islamabad', 'ISLAMABAD'),
                 ('multan', 'MULTAN'),
             )),


class Ad_Post_Form(forms.ModelForm):
    ad_title = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter Product Title', 'class': 'form-control , form-control-alternative', 'text-align':
            'center', '-ms-text-align-last': 'center',
               '-moz-text-align-last': 'center',
               'text-align-last': 'center'}), required=True)

    ad_price = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter Product Price', 'class': 'form-control , form-control-alternative', 'text-align':
            'center', '-ms-text-align-last': 'center',
               '-moz-text-align-last': 'center',
               'text-align-last': 'center'}), required=True)

    ad_phone = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter Phone Number', 'class': 'form-control , form-control-alternative', 'text-align':
            'center', '-ms-text-align-last': 'center',
               '-moz-text-align-last': 'center',
               'text-align-last': 'center'}), required=True)

    ad_condition = forms.ChoiceField(required=True, choices=choice, widget=forms.Select(
        attrs={'class': 'form-control , form-control-alternative', 'text-align':
            'center', '-ms-text-align-last': 'center',
               '-moz-text-align-last': 'center',
               'text-align-last': 'center'}),)

    ad_description = forms.CharField(widget=forms.Textarea(
        attrs={'cols': 10, 'rows': 4,'placeholder': 'What you are selling', 'class': 'form-control , form-control-alternative', 'text-align':
            'center', '-ms-text-align-last': 'center',
               '-moz-text-align-last': 'center',
               'text-align-last': 'center'}),
        required=True)



    ad_image = forms.ImageField(widget=forms.ImageField(),required=True),



    ad_location = forms.ChoiceField(required=True, choices=locations, widget=forms.Select(
        attrs={'class': 'form-control , form-control-alternative', 'text-align':
            'center', '-ms-text-align-last': 'center',
               '-moz-text-align-last': 'center',
               'text-align-last': 'center', }))

    class Meta():
        model = Used_Products
        fields = ('ad_title', 'ad_description', 'ad_condition', 'ad_price', 'ad_location', 'ad_image','ad_phone')


class Ad_Update_Form(forms.ModelForm):
    ad_title = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter Product Title', 'class': 'form-control , form-control-alternative', 'text-align':
            'center', '-ms-text-align-last': 'center',
               '-moz-text-align-last': 'center',
               'text-align-last': 'center'}), required=True)

    ad_price = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter Product Price', 'class': 'form-control , form-control-alternative', 'text-align':
            'center', '-ms-text-align-last': 'center',
               '-moz-text-align-last': 'center',
               'text-align-last': 'center'}), required=True)

    ad_condition = forms.ChoiceField(required=True, choices=choice, widget=forms.Select(
        attrs={'class': 'form-control , form-control-alternative', 'text-align':
            'center', '-ms-text-align-last': 'center',
               '-moz-text-align-last': 'center',
               'text-align-last': 'center'}),)

    ad_description = forms.CharField(widget=forms.Textarea(
        attrs={'cols': 10, 'rows': 4,'placeholder': 'What you are selling', 'class': 'form-control , form-control-alternative', 'text-align':
            'center', '-ms-text-align-last': 'center',
               '-moz-text-align-last': 'center',
               'text-align-last': 'center'}),
        required=True)



    ad_image = forms.ImageField(widget=forms.ImageField(),required=True,),



    ad_location = forms.ChoiceField(required=True, choices=locations, widget=forms.Select(
        attrs={'class': 'form-control , form-control-alternative', 'text-align':
            'center', '-ms-text-align-last': 'center',
               '-moz-text-align-last': 'center',
               'text-align-last': 'center', }))

    ad_phone = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter Phone Number', 'class': 'form-control , form-control-alternative', 'text-align':
            'center', '-ms-text-align-last': 'center',
               '-moz-text-align-last': 'center',
               'text-align-last': 'center'}), required=True)

    class Meta():
        model = Used_Products
        fields = ('ad_title', 'ad_description', 'ad_condition', 'ad_price', 'ad_location', 'ad_image','ad_phone')
