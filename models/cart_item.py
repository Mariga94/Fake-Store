#!/usr/bin/python3
"""Class CartItem that inherits from BaseModel"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class CartItem(BaseModel, Base):
    """Defines ProductCategory class
    __tablename__ (str): name of MySQL table to store cart items
    product_id (sqlalchemy.Integer): product id
    quantity (sqlalchemy Integer): product quantity 
    """
    
    __tablename__ = "cart_item"
    product_id = Column(String(60), ForeignKey('product.id'), nullable=False)
    quantity = Column(Integer, nullable=False, default=0)
    # children relationship
    product = relationship("Product", back_populates="cart_item")
    