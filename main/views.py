from django.http.response import HttpResponse
from django.shortcuts import render

from main.models import Category, Product

# Create your views here.
def index(request):
    categories = Category.objects.filter()
    return render(request, 'main/index.html', locals())

def product_list(request, slug):
    products = Product.objects.filter(category__slug=slug)
    return render(request, 'main/product_list.html', locals())
