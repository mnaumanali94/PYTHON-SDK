# -*- coding: utf-8 -*-

"""
    testerlib.http.http_call_back

    This file was automatically generated for Stamplay by APIMATIC BETA v2.0 on 08/03/2016
"""

from testerlib.http.http_request import HttpRequest
from testerlib.http.http_response import HttpResponse

class HttpCallBack(object):

    """An interface for  the callback to be called before and after the 
    HTTP call for an endpoint is made.
    
    This class should not be instantiated but should be used as a base class
    for HttpCallBack classes.  

    """

    def on_before_request(self,
                          request):
        """The controller will call this method before making the HttpRequest.
       
        Args:
            request (HttpRequest): The request object which will be sent
                to the HttpClient to be executed.
        """
        raise NotImplementedError("This method has not been implemented.")

    def on_after_response(self,
                          response):
        """The controller will call this method after making the HttpRequest.
       
        Args:
            response (HttpResponse): The HttpResponse object which the HttpClient
            returns after executing the request.
        """
        raise NotImplementedError("This method has not been implemented.")
