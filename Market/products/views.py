from django.shortcuts import render

from .models import Product, Type

type_list = Type.objects.all()


def product_list(requests):
    products = Product.objects.all()
    return render(requests, "products/product_list.html", context={"products": products, "product_type": type_list})


def product_instance(requests, pk):
    product = Product.objects.get(pk=pk)
    return render(requests, "products/product_instance.html", context={"product": product})


def filter_type(requests, type_pk):
    products = Product.objects.filter(product_type=type_pk)
    return render(requests, "products/product_list.html", context={"products": products, "product_type": type_list})
