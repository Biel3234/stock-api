from django.urls import path
from .views import ProductListView, ProductUpdateView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('editproduct/<int:pk>', ProductUpdateView.as_view()),
]