# -*- coding: utf-8 -*-

"""
    tests.controllers.test_query_param_controller

    This file was automatically generated for Stamplay by APIMATIC BETA v2.0 on 08/03/2016
"""

import jsonpickle
from tests.controllers.controller_test_base import *

class QueryParamControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(QueryParamControllerTests, cls).setUpClass()
        cls.controller = cls.api_client.query_param

    # Todo: Add description for test test_simple_query
    def test_simple_query(self):
        # Parameters for the API call
        boolean = True
        number = 4
        string = 'TestString'

        # dictionary for optional query parameters
        optional_query_parameters = {}

        # Perform the API call through the SDK function
        result = self.controller.simple_query(boolean, number, string, optional_query_parameters)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)
        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize('{"passed":true}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.raw_body)
        self.assertTrue(TestHelper.match_body(expected_body, received_body, check_values = True))


    # Todo: Add description for test test_no_params
    def test_no_params(self):

        # Perform the API call through the SDK function
        result = self.controller.no_params()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)
        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize('{"passed":true}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.raw_body)
        self.assertTrue(TestHelper.match_body(expected_body, received_body, check_values = True))


    # Todo: Add description for test test_string_param
    def test_string_param(self):
        # Parameters for the API call
        string = 'l;asd;asdwe[2304&&;\'.d??\\a\\\\\\;sd//'

        # Perform the API call through the SDK function
        result = self.controller.string_param(string)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)
        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize('{"passed":true}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.raw_body)
        self.assertTrue(TestHelper.match_body(expected_body, received_body, check_values = True))


    # Todo: Add description for test test_url_param
    def test_url_param(self):
        # Parameters for the API call
        url = 'https://www.shahidisawesome.com/and/also/a/narcissist?thisis=aparameter&another=one'

        # Perform the API call through the SDK function
        result = self.controller.url_param(url)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)
        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize('{"passed":true}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.raw_body)
        self.assertTrue(TestHelper.match_body(expected_body, received_body, check_values = True))


    # Todo: Add description for test test_multiple_params
    def test_multiple_params(self):
        # Parameters for the API call
        number = 123412312
        precision = 1112.34
        string = '""test./;";12&&3asl"";"qw1&34"///..//.'
        url = 'http://www.abc.com/test?a=b&c="http://lolol.com?param=no&another=lol"'

        # Perform the API call through the SDK function
        result = self.controller.multiple_params(number, precision, string, url)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)
        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize('{"passed":true}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.raw_body)
        self.assertTrue(TestHelper.match_body(expected_body, received_body, check_values = True))


    # Todo: Add description for test test_number_array
    def test_number_array(self):
        # Parameters for the API call
        integers = APIHelper.json_deserialize('[1,2,3,4,5]')

        # Perform the API call through the SDK function
        result = self.controller.number_array(integers)

        # Test response code
        self.assertTrue(self.response_catcher.response.status_code in list(range(200, 209)))
        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize('{"passed":true}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.raw_body)
        self.assertTrue(TestHelper.match_body(expected_body, received_body, check_values = True))


    # Todo: Add description for test test_string_array
    def test_string_array(self):
        # Parameters for the API call
        strings = APIHelper.json_deserialize('["abc", "def"]')

        # Perform the API call through the SDK function
        result = self.controller.string_array(strings)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)
        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize('{"passed":true}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.raw_body)
        self.assertTrue(TestHelper.match_body(expected_body, received_body, check_values = True))


    # Todo: Add description for test test_string_enum_array
    def test_string_enum_array(self):
        # Parameters for the API call
        days = APIHelper.json_deserialize('["Tuesday", "Saturday", "Wednesday", "Monday", "Sunday"]')

        # Perform the API call through the SDK function
        result = self.controller.string_enum_array(days)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)
        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize('{"passed":true}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.raw_body)
        self.assertTrue(TestHelper.match_body(expected_body, received_body, check_values = True))


    # Todo: Add description for test test_integer_enum_array
    def test_integer_enum_array(self):
        # Parameters for the API call
        suites = APIHelper.json_deserialize('[1, 3, 4, 2, 3]')

        # Perform the API call through the SDK function
        result = self.controller.integer_enum_array(suites)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)
        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize('{"passed":true}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.raw_body)
        self.assertTrue(TestHelper.match_body(expected_body, received_body, check_values = True))


