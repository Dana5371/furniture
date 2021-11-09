from django.urls import path

from main.views import index

from order.views import create_order
urlpatterns = [
    path('create/<int:name_of_product_id>', create_order, name='create-order'),
]