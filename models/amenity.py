#!/usr/bin/python3
"""Class defines the Amenity class and inherits from BaseModel"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity

    Attributes:
        name (str): THe name of the amenity.
    """

    name = ""
