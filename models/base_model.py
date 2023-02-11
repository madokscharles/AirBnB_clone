#!/usr/bin/python3
""" A class BaseModel that defines all common attributes/methods """

import uuid
from datetime import datetime as dt
from models import storage



class BaseModel:

    """ class BaseModel: Parent class other class inherit from """

    def __init__(self, *args, **kwargs):
        """ Initializes new instances of BaseModel calss using:
        
            Args: Arguments and 
            Kwargs: Keyword arguments
        """

        if kwargs and kwargs != {}:
            for i in kwargs:
                if i == "created_at":
                    self.__dict__["created_at"] = dt.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif i == "updated_at":
                    self.__dict__["updated_at"] = dt.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[i] = kwargs[i]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            storage.new(self)

    def __str__(self):
        """ Prints string representation """

        return ("[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__))

    def save(self):
        """ Updates the public instance attribute update_at with current time """

        self.updated_at = dt.now
        storage.save()

    def to_dict(self):
        """ Updates a dictionary containing all keys/values of __dict__ of the instance """

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dicit
