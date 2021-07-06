from django.urls import path

from Vendors import views
from Vendors.middlewares.auth import vendorPanel_middleware

urlpatterns = [
    # view main panel
    path('', vendorPanel_middleware(views.vendorpanel), name='vendorpanel'),
    path('create_store/', vendorPanel_middleware(views.create_store), name='create_store'),
    path('store_info/', vendorPanel_middleware(views.store_info), name='store_info'),
    path('updatestore/<int:id>/', views.updatestore, name='updatestore'),
    path('add_products/', vendorPanel_middleware(views.add_products), name='add_products'),
    path('update_products/<int:id>/', views.update_products, name='update_products'),
    path('deletestore/<int:id>/', views.deletestore, name='deletestore'),
    path('show_vendor_products/', vendorPanel_middleware(views.show_vendor_products), name='show_vendor_products'),
    path('delete_products/<int:id>/', views.delete_products, name='delete_products'),
    path('update_vendor_profile/', vendorPanel_middleware(views.update_vendor_profile), name='update_vendor_profile'),
    path('total_orders/', vendorPanel_middleware(views.total_orders), name='total_orders'),
    path('order_detail/<int:id>/', views.order_detail, name='order_detail'),

    path('load-cat/', views.load_cat, name='ajax_load_cat')
]
