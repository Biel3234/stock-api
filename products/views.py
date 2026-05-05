from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import F, Sum
from .models import Product, Movement
from .serializers import ProductCreateSerializer, ProductListSerializer, MovementCreateSerializer


class ProductListView(ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ProductListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ProductUpdateView(RetrieveUpdateDestroyAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer

class MovementListView(ListCreateAPIView):

    queryset = Movement.objects.all()
    serializer_class = MovementCreateSerializer

class DashboardView(APIView):

    def get(self, request):
        total_movements = Movement.objects.count()
        total_entrys = Movement.objects.filter(movement_type='IN').count()
        total_exits = Movement.objects.filter(movement_type='OUT').count()
        total_products = Product.objects.count()
        product_stock_is_low = Product.objects.filter(quantity_in_stock__lte=F('minimum_stock')).count()
        total_stock_value = Product.objects.aggregate(total = Sum(F('price') * F('quantity_in_stock')))['total']
        out_of_stock = Product.objects.filter(quantity_in_stock=0).count()
        top_products = Movement.objects.values('product__name').annotate(total = Sum('quantity'))
        data = {
            'total_movements': total_movements, 
            'total_entrys': total_entrys,
            'total_exits': total_exits,
            'total_products': total_products,
            'product_stock_is_low': product_stock_is_low,
            'total_stock_value': total_stock_value,
            'out_of_stock': out_of_stock,
            'top_products': top_products
        }
        return Response(data=data, status=status.HTTP_200_OK)

