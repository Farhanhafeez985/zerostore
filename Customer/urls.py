from django.urls import path
from Customer.middlewares.auth import customerPanel_middleware
from Customer import views

urlpatterns = [

    path('', customerPanel_middleware(views.customer_panel), name='customerpanel'),
    path('updateprofile/', customerPanel_middleware(views.profile_update), name='updateprofile'),
    path('wish_list/<int:id>/', views.wish_list, name='wish_list'),
    path('comment/<int:id>/', views.comment, name='comment'),
    path('wished_product/', views.wished_product, name='wished_product'),
    path('delete_comment/<int:id>/', views.delete_comment, name='delete_comment'),
    path('delete_wish_pro/<int:id>/', views.delete_wish_pro, name='delete_wish_pro'),

]
