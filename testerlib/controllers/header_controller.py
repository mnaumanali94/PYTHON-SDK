# -*- coding: utf-8 -*-

"""
    testerlib.controllers.header_controller

    This file was automatically generated for Stamplay by APIMATIC BETA v2.0 on 08/03/2016
"""

from testerlib.controllers.base_controller import *

from testerlib.models.server_response import ServerResponse


class HeaderController(BaseController):

    """A Controller to access Endpoints in the testerlib API."""

    def __init__(self, http_client = None, http_call_back = None):
        """Constructor which allows a different HTTP client for this controller."""
        BaseController.__init__(self, http_client, http_call_back)

    def send_headers(self,
                     custom_header,
                     value):
        """Does a POST request to /header.

        Sends a single header params

        Args:
            custom_header (string): TODO: type description here. Example: 
            value (string): Represents the value of the custom header

        Returns:
            ServerResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        if custom_header == None:
            raise ValueError("Required parameter 'custom_header' cannot be None.")
        elif value == None:
            raise ValueError("Required parameter 'value' cannot be None.")

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/header'
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'Stamplay SDK',
            'accept': 'application/json',
            'custom-header': custom_header
        }

        # Prepare form parameters
        _form_parameters = {
            'value': value
        }
        
        # Form encode parameters.
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare the API call.
        _http_request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)

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
        return APIHelper.json_deserialize(_response.raw_body, ServerResponse.from_dictionary)


