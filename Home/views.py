from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View

from Customer.models import Comments
from Seller.models import Used_Products
from Vendors.models import Products


# Create your views here.

class home(View):

    def post(self, request):
        url = request.META.get('HTTP_REFERER')
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        return redirect(url)

    def get(self, request):
        return render(request, 'home.html',{"home": "active"})


def new_prod_quick_view(request, id):
    product = Products.objects.get(id=id)
    related_products= Products.objects.filter(subcategory_id=product.subcategory.id).exclude(id=id)[:4]
    length = len(Comments.objects.filter(product_id=id))
    comment= Comments.objects.filter(product_id=id)
    context = {'product': product,'length':length,'comment':comment,'related_products':related_products}
    return render(request, 'product_quickview.html', context)


class cart(View):


    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Products.get_product_by_id(ids)
        return render(request, 'cart.html', {'products': products})


def new_products_shop(request):
    return render(request, 'new_products_shop.html')


def old_products_shop(request):
    return render(request, 'old_products_shop.html')


def old_product_quick_view(request, id):
    product = Used_Products.objects.get(id=id)
    context = {'product': product}
    return render(request, 'used_product_quick_view.html', context)


def search(request):
    search_data = request.GET.get('keyword')
    if not search_data:
        products = Products.objects.all()
        oldproducts = Used_Products.objects.all()
        return render(request, 'searched_products.html', {'products': products, 'oldproducts': oldproducts})
    else:
        products = Products.objects.filter(product_name__icontains=search_data)
        oldproducts = Used_Products.objects.filter(
            Q(ad_title__icontains=search_data) | Q(ad_location__icontains=search_data))
        return render(request, 'searched_products.html', {'products': products, 'oldproducts': oldproducts})


def search_by_cat(request):
    id = request.GET.get('cat')
    if id:
        products = Products.objects.filter(category_id=id)
        used_products = Used_Products.objects.filter(category_id=id)
        return render(request, 'searched_products.html', {'products': products, 'oldproducts': used_products})
    return render(request, 'searched_products.html')

def Sub_category_search(request):
    id = request.GET.get('subcat')
    if id:
        products = Products.objects.filter(subcategory_id=id)
        used_products = Used_Products.objects.filter(subcategory_id=id)
        return render(request, 'searched_products.html', {'products': products, 'oldproducts': used_products})
    return render(request, 'searched_products.html')

def store_prod(request):
    id = request.GET.get('store')
    if id:
        store_prod = Products.objects.filter(store_id=id)
        return render(request,'storeprod.html', {'products':store_prod})

