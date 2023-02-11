#!/usr/bin/python3
""" A class BaseModel that defines all common attributes/methods for other classes """


import uuid
from datetime import datetime



class BaseModel:
    """ class BaseModel: Parent class which other classes inherit from """
    def __init__(self, *args, **kwargs):
        """ Initializes instance of class BaseModel 

        Using *args and **kwargs arguments for the constructor

        Args: wont be used
        Kwargs: if kwargs is not empty
        """

        if kwargs and kwargs != []:
            value = kwargs["created_at"]
            self.id = kwargs["id"]
            self.created_at = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = self.created_at
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ Prints string representing the class """

        return ("[{}] ({}) {}" .format(type(self).__name__, self.id, self.__dict__))

    def save(self):
        """ Updates the public instance attribute updated_at with current datetime """

        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__ of the instance """

        __dict__ = dict(self.__dict__)
        __dict__['__class__'] = type(self).__name__
        __dict__['created_at'] = self.created_at.isoformat()
        __dict__['updated_at'] = self.updated_at.isoformat()
        return __dict__
