# -*- coding: utf-8 -*-

"""
    tests.controllers.test_error_codes_controller

    This file was automatically generated for Stamplay by APIMATIC BETA v2.0 on 08/03/2016
"""

import jsonpickle
from tests.controllers.controller_test_base import *

class ErrorCodesControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(ErrorCodesControllerTests, cls).setUpClass()
        cls.controller = cls.api_client.error_codes

    # Todo: Add description for test test_get_400
    def test_get_400(self):

        # Perform the API call through the SDK function
        with self.assertRaises(APIException):
            result = self.controller.get_400()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 400)

    # Todo: Add description for test test_get_500
    def test_get_500(self):

        # Perform the API call through the SDK function
        with self.assertRaises(APIException):
            result = self.controller.get_500()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 500)

