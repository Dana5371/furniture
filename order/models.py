from django.db import models
from main.models import Product

# Create your models here.
class Order(models.Model):
    name_of_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    phone = models.CharField(max_length=13)
    address = models.TextField()
    city = models.CharField(max_length=100)
    email = models.EmailField()
    


    def __str__(self):
        return self.name_of_product