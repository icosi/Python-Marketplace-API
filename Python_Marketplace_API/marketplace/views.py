from datetime import datetime
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict

import json
from .models import *
from .forms import *


def user_create(request):
    body = json.loads(request.body.decode('utf-8'))

    user = Users()
    user.name = body["name"]
    user.last_name = body["last_name"]
    user.save()

    cart = Carts()
    cart.user = user
    cart.save()

    return JsonResponse(model_to_dict(user), safe=False)


def user_cart(request):
    body = json.loads(request.body.decode('utf-8'))

    cart = Carts.objects.filter(user_id=body["user_id"])
    cart_json = serializers.serialize('json', cart)

    cart_id = cart.get().__dict__["cart_id"]
    cart_products = CartProductRelation.objects.filter(cart=cart_id)

    cart_json = serializers.serialize('json', cart_products)

    return JsonResponse(cart_json, safe=False)


def user_add_product(request):
    body = json.loads(request.body.decode('utf-8'))
    cart = Carts.objects.filter(user_id=body["user_id"])
    product = Products.objects.filter(product_id=body["product_id"])

    cart_id = cart.get().__dict__["cart_id"]
    product_id = product.get().__dict__["product_id"]

    added = CartProductRelation()
    added.cart_id = cart_id
    added.product_id = product_id
    added.save()

    return JsonResponse({"status": "Cart updated"}, safe=False)


def user_checkout(request):
    body = json.loads(request.body.decode('utf-8'))

    cart = Carts.objects.filter(user_id=body["user_id"])
    cart_json = serializers.serialize('json', cart)

    cart_id = cart.get().__dict__["cart_id"]
    cart_products = CartProductRelation.objects.filter(cart=cart_id)

    product_ids = get_product_ids_from_queryset(cart_products)
    cart_prices = get_prices_from_product_ids(product_ids)

    total_price = sum(cart_prices)

    CartProductRelation.objects.filter(cart=cart_id).delete()

    return JsonResponse({"total": total_price}, safe=False)


def get_product_ids_from_queryset(cart_products):
    ids = []
    for prod in cart_products:
        ids.append(prod.__dict__["product_id"])
    return ids


def get_prices_from_product_ids(product_ids):
    prices = []
    for id in product_ids:
        product = Products.objects.filter(product_id=id)
        prices.append(product.get().__dict__["price"])

    return prices


def product_all(request):
    data = list(Products.objects.values())
    return JsonResponse(data, safe=False)


def product_id(request):
    body = json.loads(request.body.decode('utf-8'))
    product_id = body["product_id"]
    product = Products.objects.filter(product_id=product_id)
    product_json = serializers.serialize('json', product)
    return JsonResponse(product_json, safe=False)


def product_new(request):
    body = json.loads(request.body.decode('utf-8'))

    prod = Products()
    prod.name = body["name"]
    prod.category = body["category"]
    prod.description = body["description"]
    prod.price = body["price"]
    prod.save()

    return JsonResponse(model_to_dict(prod), safe=False)
