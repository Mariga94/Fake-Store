#!/usr/bin/python3
"""Class User that inherit from BaseModel"""
from models.base_model import BaseModel, Base
from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship
from models.user_address import UserAddress


class User(BaseModel, Base):
    """Representation of a user"""
    
    __tablename__ = "user"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    phone_number = Column(String(128), nullable=False)

    # Relationship
    user_address = relationship("UserAddress", back_populates="user", cascade="delete")

    