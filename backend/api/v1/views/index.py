#!/usr/bin/python3
""" Index """
from models import storage
from api.v1.views import app_views
from flask import jsonify, request


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})

@app_views.route("/stats", methods=['GET'])
def stats():
    if request.method == "GET":
        response = {}
        classes = {
            'CartItem': "cart_item",
            'ProductCategory': "product_category",
            'Product': "product",
            'UserAddress': "user_address",
            'User': "user"
            }
        for key, value in classes.items():
            response[value] = storage.count(key)
        return jsonify(response)


