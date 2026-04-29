from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductCreateSerializer, ProductListSerializer


class ProductListView(ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ProductListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


