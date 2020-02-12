# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException

from avand.exception import AvandException
from examples.config import *
from avand import Avand

try:
    avand = Avand(api_token=API_TOKEN, server_type=SERVER_MODE)
    invoice_id = 123456

    print(avand.verify_invoice(invoice_id=invoice_id))
    # OUTPUT
    # True

    print("Raw Result : {}".format(avand.response.raw))
    # OUTPUT
    # Raw Result : {
    #   "hasError": false,
    #   "referenceId": 1580564631698,
    #   "errorCode": 0,
    #   "errorMessage": "",
    #   "result": {}
    # }

except AvandException as e:
    print("Error {}\nError Code : {}\nReference Id : {}".format(e.message, e.error_code, e.reference_id))
    print("Raw Result :", avand.response.raw)
except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
