#!/usr/bin/python3
""" Index """
from models import storage
from api.v1.views import app_views
from flask import jsonify, request, abort


@app_views.route('/categories', methods=['GET'])
def get_categories():
    """Get all categories"""
    response = {}
    if request.method == "GET":
        categories = storage.all('ProductCategory').values()
        categories_list = []
        for category in categories:
            categories_list.append(category.to_dict())
        return jsonify(categories_list)

@app_views.route('/categories/<category_id>', methods=['GET'])
def get_category(category_id):
    """Get category by id"""
    category = storage.get('ProductCategory', category_id)
    if category is None:
        abort(404)

    if request.method == "GET":
        return jsonify(category.to_dict())

@app_views.route("/category/<category_id>/product", methods=["GET"])
def get_category_by_product_id(category_id):
    products = []
    category = storage.get("ProductCategory", category_id)
    if not category:
        abort(404)
    for product in category.product:
        products.append(product.to_dict())
    
    return jsonify(products)