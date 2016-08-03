# -*- coding: utf-8 -*-

"""
    testerlib.models.person
 
    This file was automatically generated for Stamplay by APIMATIC v2.0 ( https://apimatic.io ) on 08/03/2016
"""

from testerlib.models.base_model import BaseModel


class Person(BaseModel):

    """Implementation of the 'Person' model.

    TODO: type model description here.

    Attributes:
        address (string): TODO: type description here.
        age (long|int): TODO: type description here.
        name (string): TODO: type description here.
        uid (string): TODO: type description here.

    """

    def __init__(self, 
                 address = None,
                 age = None,
                 name = None,
                 uid = None):
        """Constructor for the Person class"""
        
        # Initialize members of the class
        self.address = address
        self.age = age
        self.name = name
        self.uid = uid

        # Create a mapping from Model property names to API property names
        self.names = {
            "address": "address",
            "age": "age",
            "name": "name",
            "uid": "uid",
        }

    @classmethod
    def from_dictionary(cls, 
                        dictionary):
        """Creates an instance of this model from a dictionary
       
        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.
            
        Returns:
            object: An instance of this structure class.
            
        """

        if dictionary == None:
            return None
        else:	
            # Extract variables from the dictionary
            address = dictionary.get("address")
            age = dictionary.get("age")
            name = dictionary.get("name")
            uid = dictionary.get("uid")
            # Return an object of this model
            return cls(address,
                       age,
                       name,
                       uid)
