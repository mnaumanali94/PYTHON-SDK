# -*- coding: utf-8 -*-

"""
    testerlib.models.echo_response
 
    This file was automatically generated for Stamplay by APIMATIC v2.0 ( https://apimatic.io ) on 08/03/2016
"""

from testerlib.models.base_model import BaseModel


class EchoResponse(BaseModel):

    """Implementation of the 'EchoResponse' model.

    Raw http Request info

    Attributes:
        body (dict<object, object>): TODO: type description here.
        headers (dict<object, string>): TODO: type description here.
        method (string): TODO: type description here.
        path (string): relativePath
        query (dict<object, string>): TODO: type description here.
        upload_count (int): TODO: type description here.

    """

    def __init__(self, 
                 body = None,
                 headers = None,
                 method = None,
                 path = None,
                 query = None,
                 upload_count = None):
        """Constructor for the EchoResponse class"""
        
        # Initialize members of the class
        self.body = body
        self.headers = headers
        self.method = method
        self.path = path
        self.query = query
        self.upload_count = upload_count

        # Create a mapping from Model property names to API property names
        self.names = {
            "body": "body",
            "headers": "headers",
            "method": "method",
            "path": "path",
            "query": "query",
            "upload_count": "uploadCount",
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
            body = dictionary.get("body")
            headers = dictionary.get("headers")
            method = dictionary.get("method")
            path = dictionary.get("path")
            query = dictionary.get("query")
            upload_count = dictionary.get("uploadCount")
            # Return an object of this model
            return cls(body,
                       headers,
                       method,
                       path,
                       query,
                       upload_count)
