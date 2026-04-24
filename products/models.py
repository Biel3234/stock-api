from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    quantity_in_stock = models.PositiveIntegerField(default=0)
    minimum_stock = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def is_low_stock(self):
        return self.quantity_in_stock <= self.minimun_stock
    
class Movement(models.Model):
    MOVEMENTS_TYPES = [
        ('IN', 'Entry'),
        ('OUT', 'Exit'),
    ]
    
    movement_type = models.CharField(max_length=5, choices=MOVEMENTS_TYPES)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
