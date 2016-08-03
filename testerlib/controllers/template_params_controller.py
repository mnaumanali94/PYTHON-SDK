# -*- coding: utf-8 -*-

"""
    testerlib.controllers.template_params_controller

    This file was automatically generated for Stamplay by APIMATIC BETA v2.0 on 08/03/2016
"""

from testerlib.controllers.base_controller import *

from testerlib.models.echo_response import EchoResponse


class TemplateParamsController(BaseController):

    """A Controller to access Endpoints in the testerlib API."""

    def __init__(self, http_client = None, http_call_back = None):
        """Constructor which allows a different HTTP client for this controller."""
        BaseController.__init__(self, http_client, http_call_back)

    def send_string_array(self,
                          strings):
        """Does a GET request to /{strings}.

        TODO: type endpoint description here.

        Args:
            strings (list of string): TODO: type description here. Example: 

        Returns:
            EchoResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        if strings == None:
            raise ValueError("Required parameter 'strings' cannot be None.")

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/{strings}'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'strings': strings
        })
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'Stamplay SDK',
            'accept': 'application/json'
        }

        # Prepare the API call.
        _http_request = self.http_client.get(_query_url, headers=_headers)

        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_before_request(_http_request)

        # Invoke the API call  to fetch the response.
        _response = self.http_client.execute_as_string(_http_request)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_after_response(_response)

        # Endpoint error handling using HTTP status codes.
        if _response.status_code == 404:
            return None

        # Global error handling using HTTP status codes.
        self.validate_response(_response)    

        # Return appropriate type
        return APIHelper.json_deserialize(_response.raw_body, EchoResponse.from_dictionary)



    def send_integer_array(self,
                           integers):
        """Does a GET request to /{integers}.

        TODO: type endpoint description here.

        Args:
            integers (list of int): TODO: type description here. Example: 

        Returns:
            EchoResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        if integers == None:
            raise ValueError("Required parameter 'integers' cannot be None.")

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/{integers}'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'integers': integers
        })
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'Stamplay SDK',
            'accept': 'application/json'
        }

        # Prepare the API call.
        _http_request = self.http_client.get(_query_url, headers=_headers)

        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_before_request(_http_request)

        # Invoke the API call  to fetch the response.
        _response = self.http_client.execute_as_string(_http_request)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_after_response(_response)

        # Endpoint error handling using HTTP status codes.
        if _response.status_code == 404:
            return None

        # Global error handling using HTTP status codes.
        self.validate_response(_response)    

        # Return appropriate type
        return APIHelper.json_deserialize(_response.raw_body, EchoResponse.from_dictionary)


