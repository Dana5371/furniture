from django.urls import path

from main.views import index, product_list
urlpatterns = [
    path('', index, name='home'),
    path('<str:slug>/', product_list, name='product-list'),
]