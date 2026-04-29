from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name', 
            'description', 
            'category', 
            'quantity_in_stock',
            'minimum_stock',
            'price', 
            'created_at', 
            'updated_at'
            ]
        
class ProductListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only = True)
    class Meta:
        model = Product
        fields = [
            'name', 
            'description', 
            'category', 
            'quantity_in_stock', 
            'price', 
            'created_at', 
            'updated_at'
            ]
    