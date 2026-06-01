from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('shop/<int:pk>/', views.product_detail, name='product_detail'),
    path('order/<int:pk>/', views.order, name='order'),
    path('order/<int:pk>/success/',views.order_success,name='order_success')]