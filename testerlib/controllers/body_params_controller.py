# -*- coding: utf-8 -*-

"""
    testerlib.controllers.body_params_controller

    This file was automatically generated for Stamplay by APIMATIC BETA v2.0 on 08/03/2016
"""

from testerlib.controllers.base_controller import *

from testerlib.models.server_response import ServerResponse


class BodyParamsController(BaseController):

    """A Controller to access Endpoints in the testerlib API."""

    def __init__(self, http_client = None, http_call_back = None):
        """Constructor which allows a different HTTP client for this controller."""
        BaseController.__init__(self, http_client, http_call_back)

    def send_string_array(self,
                          sarray):
        """Does a POST request to /body/string.

        sends a string body param

        Args:
            sarray (list of string): TODO: type description here. Example: 

        Returns:
            ServerResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        if sarray == None:
            raise ValueError("Required parameter 'sarray' cannot be None.")

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/body/string'

        # Process optional query parameters
        _query_parameters = {
            'array': True
        }
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'Stamplay SDK',
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare the API call.
        _http_request = self.http_client.post(_query_url, headers=_headers, query_parameters=_query_parameters, parameters=APIHelper.json_serialize(sarray))

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



    def send_integer_array(self,
                           integers):
        """Does a POST request to /body/number.

        TODO: type endpoint description here.

        Args:
            integers (list of int): TODO: type description here. Example: 

        Returns:
            ServerResponse: Response from the API. 

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
        _query_builder += '/body/number'

        # Process optional query parameters
        _query_parameters = {
            'array': True
        }
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'Stamplay SDK',
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare the API call.
        _http_request = self.http_client.post(_query_url, headers=_headers, query_parameters=_query_parameters, parameters=APIHelper.json_serialize(integers))

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



    def send_model(self,
                   model):
        """Does a POST request to /body/model.

        TODO: type endpoint description here.

        Args:
            model (Employee): TODO: type description here. Example: 

        Returns:
            ServerResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        if model == None:
            raise ValueError("Required parameter 'model' cannot be None.")

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/body/model'
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'Stamplay SDK',
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare the API call.
        _http_request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(model))

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



    def send_model_array(self,
                         models):
        """Does a POST request to /body/model.

        TODO: type endpoint description here.

        Args:
            models (list of Employee): TODO: type description here. Example: 

        Returns:
            ServerResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        if models == None:
            raise ValueError("Required parameter 'models' cannot be None.")

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/body/model'

        # Process optional query parameters
        _query_parameters = {
            'array': True
        }
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'Stamplay SDK',
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare the API call.
        _http_request = self.http_client.post(_query_url, headers=_headers, query_parameters=_query_parameters, parameters=APIHelper.json_serialize(models))

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



    def send_dynamic(self,
                     dynamic):
        """Does a POST request to /body/dynamic.

        TODO: type endpoint description here.

        Args:
            dynamic (object): TODO: type description here. Example: 

        Returns:
            ServerResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        if dynamic == None:
            raise ValueError("Required parameter 'dynamic' cannot be None.")

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/body/dynamic'
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'Stamplay SDK',
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare the API call.
        _http_request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(dynamic))

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



    def send_string(self,
                    value):
        """Does a POST request to /body/string.

        TODO: type endpoint description here.

        Args:
            value (string): TODO: type description here. Example: 

        Returns:
            ServerResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        if value == None:
            raise ValueError("Required parameter 'value' cannot be None.")

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/body/string'
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'Stamplay SDK',
            'accept': 'application/json'
        }

        # Prepare the API call.
        _http_request = self.http_client.post(_query_url, headers=_headers, parameters=value)

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



    def send_string_enum_array(self,
                               days):
        """Does a POST request to /body/stringenum.

        TODO: type endpoint description here.

        Args:
            days (list of Days): TODO: type description here. Example: 

        Returns:
            ServerResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        if days == None:
            raise ValueError("Required parameter 'days' cannot be None.")

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/body/stringenum'

        # Process optional query parameters
        _query_parameters = {
            'array': True
        }
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'Stamplay SDK',
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare the API call.
        _http_request = self.http_client.post(_query_url, headers=_headers, query_parameters=_query_parameters, parameters=APIHelper.json_serialize(days))

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



    def send_integer_enum_array(self,
                                suites):
        """Does a POST request to /body/integerenum.

        TODO: type endpoint description here.

        Args:
            suites (list of SuiteCode): TODO: type description here. Example:
                
        Returns:
            ServerResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        if suites == None:
            raise ValueError("Required parameter 'suites' cannot be None.")

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/body/integerenum'

        # Process optional query parameters
        _query_parameters = {
            'array': True
        }
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'Stamplay SDK',
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare the API call.
        _http_request = self.http_client.post(_query_url, headers=_headers, query_parameters=_query_parameters, parameters=APIHelper.json_serialize(suites))

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


