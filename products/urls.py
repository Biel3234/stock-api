from django.urls import path
from .views import ProductListView, ProductUpdateView, MovementListView, DashboardView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('editproduct/<int:pk>', ProductUpdateView.as_view()),
    path('movements/', MovementListView.as_view()),
    path('dashboard/', DashboardView.as_view())
]