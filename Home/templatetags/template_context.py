from Admin.models import Categories, Sub_Categories
from Customer.models import Comments, Wishlist
from Order.models import Order
from Seller.models import Used_Products
from Signup.models import User_model, Customer_model
from Vendors.models import Products, Store


def get_filter(request):
    #all object returned
    categories = Categories.objects.all()
    subcategories = Sub_Categories.objects.all()
    products = Products.objects.all()
    oldproducts = Used_Products.objects.all()
    stores = Store.objects.all()
    users = User_model.objects.all()
    customer = Customer_model.objects.all()
    orders = Order.objects.all()

    #cart or cart list
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    ids = list(request.session.get('cart').keys())
    cart_products = Products.get_product_by_id(ids)

    #wished products count
    try:
        user_id=request.session['obj_id']
        count = len(Wishlist.objects.get(user_id=user_id).item.all())
    except:
        count = 0
    data = {'categories': categories,
            'subcategories': subcategories,
            'products': products,
            'old': oldproducts,
            'stores': stores,
            'cartpro': cart_products,
            'users': users,
            'customer': customer,
            'orders': orders,
            'count':count,
            }
    return data
