
from django.urls import path,include
from Signup import views
urlpatterns = [
    path('', views.signup, name="signup"),
    path('customer_signup/',views.customer_signup,name='customer_signup')
]