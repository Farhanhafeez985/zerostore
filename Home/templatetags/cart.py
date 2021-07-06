from django import template


register =template.Library()

@register.filter(name='in_cart')
def in_cart(product,cart):
    #print(product,cart)
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False;

@register.filter(name='quantity')
def quantity(product,cart):
    #print(product,cart)
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0;
@register.filter(name='total')
def total(product,cart):
    return product.product_price * quantity(product,cart)

@register.filter(name='total_cart_price')
def total_cart_price(products,cart):
    sum=0
    for p in products:
        sum +=total(p,cart)
    return  sum

@register.filter(name='currency')
def currency(number):
    return "₨ "+str(number)

@register.filter(name='multiply')
def multiply(number,num):
    return number * num
