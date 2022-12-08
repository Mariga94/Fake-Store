#!/usr/bin/python3
"""Class UserAddress that inherits from BaseModel"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class UserAddress(BaseModel, Base):
    """Defines ProductCategory class
    Arguments:
    """
    __tablename__ = "user_address"
    user_id = Column(String(128), ForeignKey('user.id'),nullable=False)
    address_line1 = Column(String(128), nullable=False)
    city = Column(String(128), nullable=False)
    postal_code = Column(String(128), nullable=False)
    country = Column(String(128), nullable=False)
    telephone = Column(String(128), nullable=False)
    # parent relationship
    # child relationship
    user = relationship("User", back_populates="user_address")
   