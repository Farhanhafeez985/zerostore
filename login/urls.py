
from django.urls import path,include
from login import views
urlpatterns = [
    path('',views.loginview,name="login"),
    path('logout/',views.logout,name="logout"),

]