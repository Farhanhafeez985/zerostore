"""FYP_Ostore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
# path('admin/', admin.site.urls),

    path('admin/', include('Admin.urls')),
    path('', include('Home.urls')),
    path('signup/', include('Signup.urls')),
    path('login/', include('login.urls')),
    path('vendorpanel/', include('Vendors.urls')),
    path('sellerpanel/', include('Seller.urls')),
    path('Customer/',include('Customer.urls')),
    path('Order/',include('Order.urls')),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
