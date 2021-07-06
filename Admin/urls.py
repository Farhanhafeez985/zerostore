from django.urls import path

from Admin import views
from Admin.middlewares.auth import adminPanel_middleware

urlpatterns = [
    # view main panel

    path('', views.adminlogin, name='admin'),
    path('adminlogout/', views.adminlogout, name="adminlogout"),
    path('adminpanel/', adminPanel_middleware(views.Adminpanel), name='adminpanel'),
    path('addcat/', adminPanel_middleware(views.addcat), name="addcat"),
    path('addsubcat/', adminPanel_middleware(views.addsubcat), name="addsubcat"),
    path('edit_cat/<int:id>/', views.edit_cat, name="edit_cat"),
    path('edit_subcat/<int:id>/', views.edit_Subcat, name="edit_subcat"),
    path('catdata/', adminPanel_middleware(views.catdata), name='catdata'),
    path('subcatdata/', adminPanel_middleware(views.subcatdata), name='subcatdata'),
    path('deletecat/<int:id>/', views.deletecat, name="deletecat"),
    path('deletesubcat/<int:id>/', views.deletesubcat, name="deletesubcat"),
    # order related
    path('show_order/', adminPanel_middleware(views.show_order), name='show_order'),

    # products related
    path('oldproduct/', adminPanel_middleware(views.show_oldpro), name='oldproduct'),
    path('newproduct/', adminPanel_middleware(views.show_newpro), name='newproduct'),

    path('del_new_pro/<int:id>/', views.del_new_pro, name="del_new_pro"),
    path('del_old_pro/<int:id>/', views.del_old_pro, name="del_old_pro"),

    # vendor Store related
    path('vendorstore/', adminPanel_middleware(views.show_vendors_store), name='vendorstore'),

    path('deleteusers/<int:id>/', views.deleteusers, name="deleteusers"),
    path('deletecustomer/<int:id>/', views.deletecustomer, name="deletecustomer"),

    path('showuserdata/', adminPanel_middleware(views.showuserdata), name='showuserdata'),
    path('customerinfo/', adminPanel_middleware(views.customerinfo), name='customerinfo'),

]
