from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=55, unique=True)
    slug = models.SlugField(primary_key=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='children')


    def __str__(self):
        if self.parent:
            return f'{self.parent} --> {self.title}'
        return self.title    


class Product(models.Model):
    CHOICE = (
        ('in stock', 'In stock'),
        ('out of stock', 'Out of stock'),
        ('awating', 'Awating'),
    )
    name = models.CharField(max_length=155)
    status = models.CharField(choices=CHOICE, max_length=23)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='product')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')    

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        from django.urls import reverse
        return reverse('home')    

  