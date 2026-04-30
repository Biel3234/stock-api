from rest_framework import serializers
from .models import Product, Category, Movement

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
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
        
class MovementCreateSerializer(serializers.ModelSerializer):
    product = ProductSimpleSerializer(read_only=True)
    class Meta:
        model = Movement
        fields = [
            'movement_type',
            'product',
            'quantity',
        ]
        
        