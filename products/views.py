from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
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


