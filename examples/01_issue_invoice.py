# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException

from avand.exception import AvandException
from examples.config import *
from avand import Avand

try:
    avand = Avand(api_token=API_TOKEN, server_type=SERVER_MODE)

    redirect_uri = "http://google.com"
    price = 200
    user_id = USER_ID
    business_id = BUSINESS_ID

    invoice = avand.issue_invoice(user_id=user_id, business_id=business_id, price=price, redirect_uri=redirect_uri)

    print("Invoice :\n", invoice)
    # OUTPUT
    # Invoice :
    #  {
    #   'customerInvoiceId': 9084837,
    #   'paymentUrl': 'https://pay.pod.ir/v1/pbc/payinvoice/?invoiceId=9084837&redirectUri=http://google.com'
    #  }

    print("Raw Result : {}".format(avand.response.raw))
    # OUTPUT
    # Raw Result : {
    #   "hasError": false,
    #   "referenceId": 1580564631697,
    #   "errorCode": 0,
    #   "errorMessage": "",
    #   "result": {
    #       "customerInvoiceId": 9084837,
    #       "paymentUrl": "https://pay.pod.ir/v1/pbc/payinvoice/?invoiceId=9084837&redirectUri=http://google.com"
    #   }
    # }

except AvandException as e:
    print("Error {}\nError Code : {}\nReference Id : {}".format(e.message, e.error_code, e.reference_id))
    print("Raw Result :", avand.response.raw)
except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
