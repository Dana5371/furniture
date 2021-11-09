
from django.shortcuts import redirect, render
from main.models import Product
from order.forms import CreateOrderForm
from order.models import Order


# Create your views here.
def create_order(request, name_of_product_id):
    product = Product.objects.get(id=name_of_product_id)
    order_form = CreateOrderForm(request.POST)
    print(request.POST)
    if order_form.is_valid():
        print('VALID')
        order_form.save()
        return redirect(product.get_absolut_url())
    order_form = CreateOrderForm()           
    return render(request, 'order/order.html', {'forms': order_form, 'product': product})

