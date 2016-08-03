# -*- coding: utf-8 -*-

"""
    tests.controllers.controller_test_base

    This file was automatically generated for Stamplay by APIMATIC BETA v2.0 on 08/03/2016
"""

import unittest
from testerlib.tester_client import *
from tests.test_helper import TestHelper
from tests.http_response_catcher import HttpResponseCatcher

class ControllerTestBase(unittest.TestCase):

    """All test classes inherit from this base class. It abstracts out
    common functionality and configuration variables set up."""
    
    @classmethod
    def setUpClass(cls):
        """Class method called once before running tests in a test class."""
        cls.api_client = TesterClient()
        cls.request_timeout = 60
        cls.assert_precision = 0.1

        # Set Configuration parameters for test execution
        Configuration.BASE_URI = 'http://apimatic.hopto.org:3000'


    def setUp(self):	
        """Method called once before every test in a test class."""
        self.response_catcher = HttpResponseCatcher()
        self.controller.http_call_back =  self.response_catcher

    