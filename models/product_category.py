from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Text
from sqlalchemy.orm import relationship



class ProductCategory(BaseModel, Base):
    """Defines ProductCategory class"""
    __tablename__ = "product_category"
    name = Column(String(256), nullable=False)
    description = Column(Text, nullable=False)
    product = relationship("Product", back_populates="product_category")
