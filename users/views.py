from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from .models import User
from .serializer import UserCreateSerializer, UserListSerializer

class RegisterUserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserListSerializer(queryset, many=True)
        return Response(serializer.data)