# -*- coding: utf-8 -*-

"""
    tests.controllers.test_response_types_controller

    This file was automatically generated for Stamplay by APIMATIC BETA v2.0 on 08/03/2016
"""

import jsonpickle
from tests.controllers.controller_test_base import *

class ResponseTypesControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(ResponseTypesControllerTests, cls).setUpClass()
        cls.controller = cls.api_client.response_types

    # Todo: Add description for test test_get_long
    def test_get_long(self):

        # Perform the API call through the SDK function
        result = self.controller.get_long()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)
        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        self.assertEqual('5147483647', self.response_catcher.response.raw_body)


    # Todo: Add description for test test_get_model
    def test_get_model(self):

        # Perform the API call through the SDK function
        result = self.controller.get_model()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)
        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize('{"name":"Shahid Khaliq","age":5147483645,"address":"H # 531, S # 20","uid":"123321","salary":20000,"department":"Software Development","joiningDay":"Saturday","workingDays":["Monday","Tuesday","Friday"],"boss":{"name":"Zeeshan Ejaz","age":5147483647,"address":"I-9/1","uid":"241123"},"dependents":[{"name":"Future Wife","age":5147483649,"address":"H # 531, S # 20","uid":"123412"},{"name":"Future Kid","age":5147483648,"address":"H # 531, S # 20","uid":"312341"}]}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.raw_body)
        self.assertTrue(TestHelper.match_body(expected_body, received_body, check_values = True))


    # Todo: Add description for test test_get_string_enum_array
    def test_get_string_enum_array(self):

        # Perform the API call through the SDK function
        result = self.controller.get_string_enum_array()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)
        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize('["Tuesday", "Saturday", "Wednesday", "Monday", "Sunday"]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.raw_body)
        self.assertTrue(TestHelper.match_body(expected_body, received_body))


    # Todo: Add description for test test_get_string_enum
    def test_get_string_enum(self):

        # Perform the API call through the SDK function
        result = self.controller.get_string_enum()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)
        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        self.assertEqual('Monday', self.response_catcher.response.raw_body)


    # Todo: Add description for test test_get_model_array
    def test_get_model_array(self):

        # Perform the API call through the SDK function
        result = self.controller.get_model_array()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)
        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize('[{"name":"Shahid Khaliq","age":5147483645,"address":"H # 531, S # 20","uid":"123321","salary":20000,"department":"Software Development","joiningDay":"Saturday","workingDays":["Monday","Tuesday","Friday"],"boss":{"name":"Zeeshan Ejaz","age":5147483647,"address":"I-9/1","uid":"241123"},"dependents":[{"name":"Future Wife","age":5147483649,"address":"H # 531, S # 20","uid":"123412"},{"name":"Future Kid","age":5147483648,"address":"H # 531, S # 20","uid":"312341"}]}, {"name":"Shahid Khaliq","age":5147483645,"address":"H # 531, S # 20","uid":"123321","salary":20000,"department":"Software Development","joiningDay":"Saturday","workingDays":["Monday","Tuesday","Friday"],"boss":{"name":"Zeeshan Ejaz","age":5147483647,"address":"I-9/1","uid":"241123"},"dependents":[{"name":"Future Wife","age":5147483649,"address":"H # 531, S # 20","uid":"123412"},{"name":"Future Kid","age":5147483648,"address":"H # 531, S # 20","uid":"312341"}]}]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.raw_body)
        self.assertTrue(TestHelper.match_body(expected_body, received_body, check_values = True))


    # Todo: Add description for test test_get_int_enum
    def test_get_int_enum(self):

        # Perform the API call through the SDK function
        result = self.controller.get_int_enum()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)
        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        self.assertEqual('3', self.response_catcher.response.raw_body)


    # Todo: Add description for test test_get_int_enum_array
    def test_get_int_enum_array(self):

        # Perform the API call through the SDK function
        result = self.controller.get_int_enum_array()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)
        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize('[1, 3, 4, 2, 3]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.raw_body)
        self.assertTrue(TestHelper.match_body(expected_body, received_body))


    # Todo: Add description for test test_get_precision
    def test_get_precision(self):

        # Perform the API call through the SDK function
        result = self.controller.get_precision()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)
        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        self.assertEqual('4.999', self.response_catcher.response.raw_body)


    # Todo: Add description for test test_get_binary
    def test_get_binary(self):

        # Perform the API call through the SDK function
        result = self.controller.get_binary()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)
        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        self.assertEqual(TestHelper.get_file('https://dl.dropboxusercontent.com/u/31838656/binary.png').read(), self.response_catcher.response.raw_body)


    # Todo: Add description for test test_get_integer
    def test_get_integer(self):

        # Perform the API call through the SDK function
        result = self.controller.get_integer()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)
        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        self.assertEqual('4', self.response_catcher.response.raw_body)


    # Todo: Add description for test test_get_integer_array
    def test_get_integer_array(self):

        # Perform the API call through the SDK function
        result = self.controller.get_integer_array()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)
        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize('[1,2,3,4,5]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.raw_body)
        self.assertTrue(TestHelper.match_body(expected_body, received_body))


    # Todo: Add description for test test_get_dynamic
    def test_get_dynamic(self):

        # Perform the API call through the SDK function
        result = self.controller.get_dynamic()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)
        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize('{"method":"GET","body":{},"uploadCount":0}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.raw_body)
        self.assertTrue(TestHelper.match_body(expected_body, received_body, check_values = True))


    # Todo: Add description for test test_get_dynamic_array
    def test_get_dynamic_array(self):

        # Perform the API call through the SDK function
        result = self.controller.get_dynamic_array()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)
        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize('{"method":"GET","body":{},"uploadCount":0}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.raw_body)
        self.assertTrue(TestHelper.match_body(expected_body, received_body, check_values = True))


    # Todo: Add description for test test_get_datetime
    def test_get_datetime(self):

        # Perform the API call through the SDK function
        result = self.controller.get_datetime()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)
        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        self.assertEqual('2016-03-13T12:52:32.123Z', self.response_catcher.response.raw_body)


    # Todo: Add description for test test_get_datetime_array
    def test_get_datetime_array(self):

        # Perform the API call through the SDK function
        result = self.controller.get_datetime_array()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)
        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize('["2016-03-13T12:52:32.123Z","2016-03-13T12:52:32.123Z","2016-03-13T12:52:32.123Z"]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.raw_body)
        self.assertTrue(TestHelper.match_body(expected_body, received_body))


    # Todo: Add description for test test_get_boolean
    def test_get_boolean(self):

        # Perform the API call through the SDK function
        result = self.controller.get_boolean()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)
        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        self.assertEqual('true', self.response_catcher.response.raw_body)


    # Todo: Add description for test test_get_boolean_array
    def test_get_boolean_array(self):

        # Perform the API call through the SDK function
        result = self.controller.get_boolean_array()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)
        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize('[true, false, true, true, false]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.raw_body)
        self.assertTrue(TestHelper.match_body(expected_body, received_body))


    # Todo: Add description for test test_get_headers_allow_extra
    def test_get_headers_allow_extra(self):

        # Perform the API call through the SDK function
        self.controller.get_headers()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['naumanali'] = None
        expected_headers['waseemhasan'] = None
        
        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))


