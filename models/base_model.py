"""
This module defines all common attributes/methods for other classes
"""
import uuid  # imports uuid module
from datetime import datetime  # imports datetime class from datetime module


class BaseModel:
    """
    Class doc string
    Attributes:
        - id (string): goal is to have unique id for each BaseModel
        - created_at (datetime): assign with the current datetime when an instance is created
        - updated_at (datetime): assign with the current datetime when an instance is created,
          and it will be updated every time you change your object

    """

    def __init__(self):
        """ class constructor """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ string representation of created object """
        return "[{}] ({}) ({})".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary representation of the instance, ie
        returns a dictionary containing all keys/values of __dict__ of the instance """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()  # converting to string object in iso format
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
