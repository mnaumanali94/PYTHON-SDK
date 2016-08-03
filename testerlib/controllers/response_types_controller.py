# -*- coding: utf-8 -*-

"""
    testerlib.controllers.response_types_controller

    This file was automatically generated for Stamplay by APIMATIC BETA v2.0 on 08/03/2016
"""

import dateutil.parser
from testerlib.controllers.base_controller import *

from testerlib.models.employee import Employee
from testerlib.models.days import Days
from testerlib.models.suite_code import SuiteCode


class ResponseTypesController(BaseController):

    """A Controller to access Endpoints in the testerlib API."""

    def __init__(self, http_client = None, http_call_back = None):
        """Constructor which allows a different HTTP client for this controller."""
        BaseController.__init__(self, http_client, http_call_back)

    def get_long(self):
        """Does a GET request to /response/long.

        TODO: type endpoint description here.

        Returns:
            long|int: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/response/long'
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'Stamplay SDK'
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
        return int(_response.raw_body)



    def get_model(self):
        """Does a GET request to /response/model.

        TODO: type endpoint description here.

        Returns:
            Employee: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/response/model'
        
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
        return APIHelper.json_deserialize(_response.raw_body, Employee.from_dictionary)



    def get_string_enum_array(self):
        """Does a GET request to /response/enum.

        TODO: type endpoint description here.

        Returns:
            list of Days: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/response/enum'

        # Process optional query parameters
        _query_parameters = {
            'array': True,
            'type': 'string'
        }
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'Stamplay SDK',
            'accept': 'application/json'
        }

        # Prepare the API call.
        _http_request = self.http_client.get(_query_url, headers=_headers, query_parameters=_query_parameters)

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
        return APIHelper.json_deserialize(_response.raw_body)



    def get_string_enum(self):
        """Does a GET request to /response/enum.

        TODO: type endpoint description here.

        Returns:
            Days: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/response/enum'

        # Process optional query parameters
        _query_parameters = {
            'type': 'string'
        }
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'Stamplay SDK'
        }

        # Prepare the API call.
        _http_request = self.http_client.get(_query_url, headers=_headers, query_parameters=_query_parameters)

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
        return _response.raw_body



    def get_model_array(self):
        """Does a GET request to /response/model.

        TODO: type endpoint description here.

        Returns:
            list of Employee: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/response/model'

        # Process optional query parameters
        _query_parameters = {
            'array': True
        }
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'Stamplay SDK',
            'accept': 'application/json'
        }

        # Prepare the API call.
        _http_request = self.http_client.get(_query_url, headers=_headers, query_parameters=_query_parameters)

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
        return APIHelper.json_deserialize(_response.raw_body, Employee.from_dictionary)



    def get_int_enum(self):
        """Does a GET request to /response/enum.

        TODO: type endpoint description here.

        Returns:
            SuiteCode: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/response/enum'

        # Process optional query parameters
        _query_parameters = {
            'type': 'int'
        }
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'Stamplay SDK'
        }

        # Prepare the API call.
        _http_request = self.http_client.get(_query_url, headers=_headers, query_parameters=_query_parameters)

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
        return int(_response.raw_body)



    def get_int_enum_array(self):
        """Does a GET request to /response/enum.

        TODO: type endpoint description here.

        Returns:
            list of SuiteCode: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/response/enum'

        # Process optional query parameters
        _query_parameters = {
            'array': True,
            'type': 'int'
        }
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'Stamplay SDK',
            'accept': 'application/json'
        }

        # Prepare the API call.
        _http_request = self.http_client.get(_query_url, headers=_headers, query_parameters=_query_parameters)

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
        return APIHelper.json_deserialize(_response.raw_body)



    def get_precision(self):
        """Does a GET request to /response/precision.

        TODO: type endpoint description here.

        Returns:
            float: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/response/precision'
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'Stamplay SDK'
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
        return float(_response.raw_body)



    def get_binary(self):
        """Does a GET request to /response/binary.

        gets a binary object

        Returns:
            binary: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/response/binary'
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'Stamplay SDK'
        }

        # Prepare the API call.
        _http_request = self.http_client.get(_query_url, headers=_headers)

        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_before_request(_http_request)

        # Invoke the API call  to fetch the response.
        _response = self.http_client.execute_as_binary(_http_request)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_after_response(_response)

        # Endpoint error handling using HTTP status codes.
        if _response.status_code == 404:
            return None

        # Global error handling using HTTP status codes.
        self.validate_response(_response)    

        # Return appropriate type
        return _response.raw_body



    def get_integer(self):
        """Does a GET request to /response/integer.

        Gets a integer response

        Returns:
            int: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/response/integer'
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'Stamplay SDK'
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
        return int(_response.raw_body)



    def get_integer_array(self):
        """Does a GET request to /response/integer.

        Get an array of integers.

        Returns:
            list of int: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/response/integer'

        # Process optional query parameters
        _query_parameters = {
            'array': True
        }
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'Stamplay SDK',
            'accept': 'application/json'
        }

        # Prepare the API call.
        _http_request = self.http_client.get(_query_url, headers=_headers, query_parameters=_query_parameters)

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
        return APIHelper.json_deserialize(_response.raw_body)



    def get_dynamic(self):
        """Does a GET request to /response/dynamic.

        TODO: type endpoint description here.

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/response/dynamic'
        
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
        return APIHelper.json_deserialize(_response.raw_body)



    def get_dynamic_array(self):
        """Does a GET request to /response/dynamic.

        TODO: type endpoint description here.

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/response/dynamic'

        # Process optional query parameters
        _query_parameters = {
            'array': True
        }
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'Stamplay SDK',
            'accept': 'application/json'
        }

        # Prepare the API call.
        _http_request = self.http_client.get(_query_url, headers=_headers, query_parameters=_query_parameters)

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
        return APIHelper.json_deserialize(_response.raw_body)



    def get_datetime(self):
        """Does a GET request to /response/datetime.

        TODO: type endpoint description here.

        Returns:
            DateTime: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/response/datetime'
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'Stamplay SDK'
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
        return dateutil.parser.parse(_response.raw_body)



    def get_datetime_array(self):
        """Does a GET request to /response/datetime.

        TODO: type endpoint description here.

        Returns:
            list of DateTime: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/response/datetime'

        # Process optional query parameters
        _query_parameters = {
            'array': True
        }
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'Stamplay SDK',
            'accept': 'application/json'
        }

        # Prepare the API call.
        _http_request = self.http_client.get(_query_url, headers=_headers, query_parameters=_query_parameters)

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
        return APIHelper.json_deserialize(_response.raw_body, dateutil.parser.parse)



    def get_boolean(self):
        """Does a GET request to /response/boolean.

        TODO: type endpoint description here.

        Returns:
            bool: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/response/boolean'
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'Stamplay SDK'
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
        return _response.raw_body == 'true'



    def get_boolean_array(self):
        """Does a GET request to /response/boolean.

        TODO: type endpoint description here.

        Returns:
            list of bool: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/response/boolean'

        # Process optional query parameters
        _query_parameters = {
            'array': True
        }
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'Stamplay SDK',
            'accept': 'application/json'
        }

        # Prepare the API call.
        _http_request = self.http_client.get(_query_url, headers=_headers, query_parameters=_query_parameters)

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
        return APIHelper.json_deserialize(_response.raw_body)



    def get_headers(self):
        """Does a GET request to /response/headers.

        TODO: type endpoint description here.

        Returns:
            void: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/response/headers'
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'Stamplay SDK'
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

        # Global error handling using HTTP status codes.
        self.validate_response(_response)    
