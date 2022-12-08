#!/usr/bin/python3
""" Index """
from models import storage
from models.cart_item import CartItem
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
import json

@app_views.route('/cart', methods=['GET'])
def get_cart_items():
    """Retrieves the list of products"""
    cart_items = storage.all("CartItem").values()
    lst = []
    for cart_item in cart_items: 
        product = cart_item.product.to_dict()
        product["cart_item_id"] = cart_item.id
        product["quantity"] = cart_item.quantity
        lst.append(product)
    return jsonify(lst)
   # lst.append(cart_item.product.to_dict())

@app_views.route('/cart/<product_id>', methods=['POST'])
def post_cart_items(product_id):
    # "Post product to cart"
    product = storage.get('Product', product_id)
    data = request.get_json(silent=True)
    if not product:
        abort(404) 
    if not data:
        abort(400, description="Not a JSON")

    instance = CartItem(**data)
    instance.product_id = product_id
    instance.quantity = 1
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/cart/<cart_item_id>', methods=['DELETE'])
def remove_item(cart_item_id):
    cart_item = storage.get("CartItem", cart_item_id)
    cart_item.delete()
    storage.save()
    return ({})