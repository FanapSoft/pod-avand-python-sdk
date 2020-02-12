# coding=utf-8
from __future__ import unicode_literals

import unittest

from pod_base import InvalidDataException

from avand import Avand
from tests.config import *


class TestAvand(unittest.TestCase):
    __slots__ = "__avand"

    def setUp(self):
        self.__avand = Avand(api_token=API_TOKEN, server_type=SERVER_MODE)

    def test_01_issue_invoice(self):
        result = self.__avand.issue_invoice(user_id=USER_ID, business_id=BUSINESS_ID, price=100,
                                            redirect_uri="http://google.ocm")
        self.assertIsInstance(result, dict, msg="issue invoice : check instance")
        self.assertIsInstance(result["customerInvoiceId"], int, msg="issue invoice : check customer invoice id")

    def test_01_issue_invoice_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="issue invoice : validation error"):
            self.__avand.issue_invoice(user_id=str(USER_ID), business_id=BUSINESS_ID, price="100",
                                       redirect_uri="abcd")

    def test_01_issue_invoice_required_params(self):
        with self.assertRaises(TypeError, msg="issue invoice : required params"):
            self.__avand.issue_invoice()

    def test_02_verify_invoice_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="verify invoice : validation error"):
            self.__avand.verify_invoice(invoice_id="123456")

    def test_03_cancel_invoice_required_params(self):
        with self.assertRaises(TypeError, msg="cancel invoice : required params"):
            self.__avand.cancel_invoice()

    def test_03_cancel_invoice_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="cancel invoice : validation error"):
            self.__avand.cancel_invoice(invoice_id="123465")

    def test_03_cancel_invoice(self):
        invoice = self.__avand.issue_invoice(user_id=USER_ID, business_id=BUSINESS_ID, price=100,
                                             redirect_uri="http://google.ocm")

        result = self.__avand.cancel_invoice(invoice_id=invoice["customerInvoiceId"])

        self.assertEqual(result, True, msg="cancel invoice : check instance")
        
    def test_04_get_invoice_list(self):
        invoices = self.__avand.get_invoice_list()
        self.assertIsInstance(invoices, list, msg="get invoice list : check instance")

    def test_04_get_invoice_list_all_params(self):
        params = {
            "page": 1,
            "size": 10,
            "id": 123456,
            "fromDate": "1398/01/01 00:00:00",  # تاریخ شمسی صدور فاکتور yyyy/mm/dd hh:mi:ss
            "toDate": "1398/12/29 00:00:00",  # تاریخ شمسی صدور فاکتور yyyy/mm/dd hh:mi:ss
            "isCanceled": True,
            "isPayed": True,
            "isClosed": True,
            "isWaiting": True,
            "userId": USER_ID  # شناسه کاربری مشتری
        }

        invoices = self.__avand.get_invoice_list(**params)
        self.assertIsInstance(invoices, list, msg="get invoice list ( all params ) : check instance")

    def test_04_get_invoice_list_first_id(self):
        params = {
            "firstId": 0
        }

        invoices = self.__avand.get_invoice_list(**params)
        self.assertIsInstance(invoices, list, msg="get invoice list ( first id ) : check instance")

    def test_04_get_invoice_list_last_id(self):
        params = {
            "lastId": 0
        }

        invoices = self.__avand.get_invoice_list(**params)
        self.assertIsInstance(invoices, list, msg="get invoice list ( last id ) : check instance")

    def test_04_get_invoice_list_validation_error(self):
        params = {
            "lastId": 0,
            "firstId": 0
        }
        with self.assertRaises(InvalidDataException, msg="get invoice list (validation error) : set first id, last id"):
            self.__avand.get_invoice_list(**params)