# -*- coding: utf-8 -*-

"""
    testerlib.models.server_response
 
    This file was automatically generated for Stamplay by APIMATIC v2.0 ( https://apimatic.io ) on 08/03/2016
"""

from testerlib.models.base_model import BaseModel


class ServerResponse(BaseModel):

    """Implementation of the 'ServerResponse' model.

    TODO: type model description here.

    Attributes:
        input (dict<object, object>): TODO: type description here.
        message (string): TODO: type description here.
        passed (bool): TODO: type description here.

    """

    def __init__(self, 
                 input = None,
                 message = None,
                 passed = None):
        """Constructor for the ServerResponse class"""
        
        # Initialize members of the class
        self.input = input
        self.message = message
        self.passed = passed

        # Create a mapping from Model property names to API property names
        self.names = {
            "input": "input",
            "message": "Message",
            "passed": "passed",
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
            input = dictionary.get("input")
            message = dictionary.get("Message")
            passed = dictionary.get("passed")
            # Return an object of this model
            return cls(input,
                       message,
                       passed)
