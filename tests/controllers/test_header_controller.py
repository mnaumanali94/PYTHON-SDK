# -*- coding: utf-8 -*-

"""
    tests.controllers.test_header_controller

    This file was automatically generated for Stamplay by APIMATIC BETA v2.0 on 08/03/2016
"""

import jsonpickle
from tests.controllers.controller_test_base import *

class HeaderControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(HeaderControllerTests, cls).setUpClass()
        cls.controller = cls.api_client.header

    # Todo: Add description for test test_send_headers
    def test_send_headers(self):
        # Parameters for the API call
        custom_header = 'TestString'
        value = 'TestString'

        # Perform the API call through the SDK function
        result = self.controller.send_headers(custom_header, value)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)
        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize('{"passed":true}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.raw_body)
        self.assertTrue(TestHelper.match_body(expected_body, received_body, check_values = True))


