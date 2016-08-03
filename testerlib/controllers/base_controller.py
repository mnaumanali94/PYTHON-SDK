# -*- coding: utf-8 -*-

"""
    testerlibcontrollers.base_controller

    This file was automatically generated for Stamplay by APIMATIC BETA v2.0 on 08/03/2016
"""

from testerlib.api_helper import APIHelper
from testerlib.api_exception import APIException
from testerlib.configuration import Configuration
from testerlib.http.http_request import HttpRequest
from testerlib.http.http_response import HttpResponse
from testerlib.http.requests_client import RequestsClient

class BaseController(object):

    """All controllers inherit from this base class. It manages shared 
	HTTP clients and global API errors."""
    
    http_call_back = None
    http_client = RequestsClient()

    def __init__(self, client, call_back):
        if client != None:
            self.http_client = client
        if call_back != None:
            self.http_call_back = call_back

    def validate_response(self, response):
        """Validates an HTTP response by checking for global errors.
       
        Args:
            response (HttpResponse): The HttpResponse object to validate.            
            
        """
        if response.status_code == 400:
            raise APIException("400 Global", response.status_code, response.raw_body)
        elif response.status_code == 500:
            raise APIException("500 Global", response.status_code, response.raw_body)
        elif (response.status_code < 200) or (response.status_code > 208): #[200,208] = HTTP OK
            raise APIException("HTTP Response Not OK", response.status_code, response.raw_body)
