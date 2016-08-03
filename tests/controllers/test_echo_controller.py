# -*- coding: utf-8 -*-

"""
    tests.controllers.test_echo_controller

    This file was automatically generated for Stamplay by APIMATIC BETA v2.0 on 08/03/2016
"""

import jsonpickle
from tests.controllers.controller_test_base import *

class EchoControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(EchoControllerTests, cls).setUpClass()
        cls.controller = cls.api_client.echo

    # Todo: Add description for test test_json_echo
    def test_json_echo(self):
        # Parameters for the API call
        input = APIHelper.json_deserialize('{"uid": "1123213", "name": "Shahid"}')

        # Perform the API call through the SDK function
        result = self.controller.json_echo(input)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)
        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize('{"body": {"uid": "1123213", "name": "Shahid"}}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.raw_body)
        self.assertTrue(TestHelper.match_body(expected_body, received_body, check_values = True))


    # Todo: Add description for test test_form_echo
    def test_form_echo(self):
        # Parameters for the API call
        input = APIHelper.json_deserialize('{"uid": "1123213", "name": "Shahid"}')

        # Perform the API call through the SDK function
        result = self.controller.form_echo(input)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)
        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize('{"body":{"input":{"uid":"1123213","name":"Shahid"}}}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.raw_body)
        self.assertTrue(TestHelper.match_body(expected_body, received_body, check_values = True))


    # Todo: Add description for test test_query_echo
    def test_query_echo(self):

        # dictionary for optional query parameters
        optional_query_parameters = {}
        optional_query_parameters['hello'] =  'world'

        # Perform the API call through the SDK function
        result = self.controller.query_echo(optional_query_parameters)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)
        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize('{"query":{"hello":"world"}}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.raw_body)
        self.assertTrue(TestHelper.match_body(expected_body, received_body, check_values = True))


