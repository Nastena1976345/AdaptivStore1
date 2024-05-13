from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>', views.product_instance, name='product_instance'),
    path('product_filter/<int:type_pk>', views.filter_type, name='product_filter'),
]
