#!/usr/bin/python3
""" Index """
from models import storage
from api.v1.views import app_views
from flask import jsonify, abort, request


@app_views.route('/products', methods=['GET'])
def get_products():
    """Retrieves the list of products"""
    products = storage.all("Product").values()
    lst = []
    for product in products:
        lst.append(product.to_dict())
    return jsonify(lst)

@app_views.route('/products/<product_id>', methods=["GET"])
def get_product(product_id):
    """Retrieve one product"""
    product = storage.get("Product", product_id)
    return jsonify(product.to_dict())