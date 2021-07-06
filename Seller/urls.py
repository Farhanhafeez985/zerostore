from django.urls import path
from Seller.middlewares.auth import sellerPanel_middleware
from Seller import views

urlpatterns = [
    # view main panel
    path('', sellerPanel_middleware(views.sellerpanel), name='sellerpanel'),
    path('edit_profile/', sellerPanel_middleware(views.edit_profile), name='edit_profile'),
    path('ad_post/', sellerPanel_middleware(views.ad_post), name='ad_post'),
    path('your_ads/', sellerPanel_middleware(views.your_ads), name='your_ads'),
    path('delete_ad/<int:id>/', views.delete_ad, name='delete_ad'),
    path('edit_ad/<int:id>/',views.edit_ad, name='edit_ad'),
]
