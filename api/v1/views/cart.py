#!/usr/bin/python3
""" Index """
from models import storage
from models.cart_item import CartItem
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response


@app_views.route('/cart', methods=['GET'])
def get_cart_items():
    """Retrieves the list of products"""
    cart_items = storage.all("CartItem").values()
    lst = []
    for cart_item in cart_items:
        lst.append(cart_item.to_dict())
    return jsonify(lst)

@app_views.route('/cart/<product_id>', methods=[''])
def create_cart_items(product_id):
    "Post product to cart"
    product = storage.get('Product', product_id)
    if not product:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")

    data = request.get_json()
    instance = CartItem(**data)
    instance.product_id = product_id
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)