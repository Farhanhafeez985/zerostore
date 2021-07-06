from django.urls import path

from Home import views
from Home.views import home, cart

urlpatterns = [

    path('', home.as_view(), name="home"),
    path('cart/', cart.as_view(), name="cart"),
    path('quick_view/<int:id>/', views.new_prod_quick_view, name="quick_view"),
    path('new_products_shop/', views.new_products_shop, name="new_products_shop"),
    path('old_products_shop/', views.old_products_shop, name="old_products_shop"),
    path('used_quickview/<int:id>', views.old_product_quick_view, name="used_quickview"),
    path('search/', views.search,name='search'),
    path('category_search/', views.search_by_cat,name='category_search'),
    path('Sub_category_search/', views.Sub_category_search,name='Sub_category_search'),
    path('storeprod/', views.store_prod,name='storeprod'),

]
