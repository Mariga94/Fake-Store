from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from models.base_model import Base
from models import product_category
from models import cart_item
from models import user_address
from models import product
from models import user

classes = {
            
            'ProductCategory': product_category.ProductCategory,
            'Product': product.Product,
            'User': user.User,
            'UserAddress': user_address.UserAddress,
            'CartItem': cart_item.CartItem
            }

class DBStorage:
    """Defines the DBStorage class"""

    # current database connection
    __engine = None
    # curent database session
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        self.__engine = create_engine("mysql+mysqldb://root:Bwambui1994#@localhost:3306/furnish_db",
                                      pool_pre_ping=True)
    
    def all(self, cls=None):
        """Query on the current database session(self.__session)
        all objects depending of the class name
        Arguments:
            cls (Instance): class name
        """
        dictionary = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    dictionary[key] = obj
        return (dictionary)


    def new(self, obj):
        """Add the object to the current database session(self.__session)"""
        if obj is not None:
            self.__session.add(obj)
    
    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()
    
    def delete(self, obj=None):
        """Delete the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(
                bind=self.__engine,
                expire_on_commit=False))

    def get(self, cls, id):
        """Retrieve one object
        Arguments:
          cls (str): class
          id (str): string representing the object ID
        """
        if cls and id:
            objs = self.all(cls)
            obj = "{}.{}".format(cls, id)
            return objs[obj]
        else:
            return None
    
    def count(self, cls=None):
        """
        Count the number of obj
        """
        return (len(self.all(cls)))

    def close(self):
        self.__session.remove()

