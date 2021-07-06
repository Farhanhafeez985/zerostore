from django.urls import path,include
from Order.middleware.auth import checkout_middleware
from Order import views
from Order.views import checkout


urlpatterns = [
    path('', checkout_middleware(views.checkout), name="checkout"),
]