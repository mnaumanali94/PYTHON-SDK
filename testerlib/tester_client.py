# -*- coding: utf-8 -*-

"""
    testerlib.tester_client

    This file was automatically generated for Stamplay by APIMATIC BETA v2.0 on 08/03/2016
"""

from testerlib.http import *
from testerlib.models import *
from testerlib.controllers import *
from testerlib.decorators import *
from testerlib.api_exception import *

class TesterClient(object):

    @lazy_property
    def response_types(self):
        return ResponseTypesController()

    @lazy_property
    def error_codes(self):
        return ErrorCodesController()

    @lazy_property
    def body_params(self):
        return BodyParamsController()

    @lazy_property
    def form_params(self):
        return FormParamsController()

    @lazy_property
    def echo(self):
        return EchoController()

    @lazy_property
    def header(self):
        return HeaderController()

    @lazy_property
    def query_param(self):
        return QueryParamController()

    @lazy_property
    def template_params(self):
        return TemplateParamsController()



