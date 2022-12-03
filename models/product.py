from models.base_model import BaseModel, Base
from sqlalchemy import String, Float, Column, Text, ForeignKey
from sqlalchemy.orm import relationship

class Product(BaseModel, Base):
    __tablename__ = "product"
    name = Column(String(256), nullable=False)
    description= Column(Text, nullable=False)
    price = Column(Float, nullable=False, default=0)
    image = Column(Text, nullable=False)
    category_id = Column(String(60), ForeignKey('product_category.id'), nullable=False)
    
    # children relationship
    product_category = relationship("ProductCategory", back_populates="product")
    # parent relationship
    cart_item = relationship("CartItem", back_populates="product")