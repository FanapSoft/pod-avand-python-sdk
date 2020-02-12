# coding=utf-8
from pod_base import APIException, PodException
from examples.config import *
from avand import Avand

try:
    avand = Avand(api_token=API_TOKEN, server_type=SERVER_MODE)

    params = {
        "isPayed": False,
        "isClosed": False,
        "isWaiting": True,
        "isCanceled": False,
        "fromDate": "1398/06/01 13:00:00",
        "toDate": "1398/06/02 17:00:00",
    }

    invoices = avand.get_invoice_list(page=1, **params)
    print("Invoices :\n", invoices)
    print("Total Invoice :", avand.total_items())

    invoices = avand.get_invoice_list(page=1)
    print("Invoices :\n", invoices)
    print("Total Invoice :", avand.total_items())
    # OUTPUT
    # Invoices :
    #  [
    #   {
    #     "id": 32157,
    #     "totalAmountWithoutDiscount": 15,
    #     "delegationAmount": 0,
    #     "totalAmount": 15,
    #     "payableAmount": 16.35,
    #     "vat": 1.35,
    #     "issuanceDate": 1566630237976,
    #     "deliveryDate": 1566588600000,
    #     "billNumber": "99",
    #     "paymentBillNumber": "1029779",
    #     "uniqueNumber": "6a8419e0de989b8f",
    #     "description": "فاکتور با شناسه قبض اجباری",
    #     "paymentDate": 0,
    #     "payed": false,
    #     "serial": 0,
    #     "canceled": false,
    #     "cancelDate": 0,
    #     "business": {
    #       "id": 7867,
    #       "name": "شرکت رضا",
    #       "numOfProducts": 370,
    #       "rate": {
    #         "rate": 8,
    #         "rateCount": 1
    #       },
    #       "sheba": "640170000000108211752007"
    #     },
    #     "invoiceItemSrvs": [
    #       {
    #         "id": 34506,
    #         "productSrv": {
    #           "id": 0,
    #           "version": 20,
    #           "timelineId": 0,
    #           "entityId": 29988,
    #           "numOfLikes": 0,
    #           "numOfDisLikes": 0,
    #           "numOfFavorites": 0,
    #           "numOfComments": 0,
    #           "timestamp": 0,
    #           "enable": false,
    #           "hide": false,
    #           "business": {
    #             "id": 7867,
    #             "name": "شرکت رضا",
    #             "numOfProducts": 370,
    #             "rate": {
    #               "rate": 8,
    #               "rateCount": 1
    #             },
    #             "sheba": "640170000000108211752007"
    #           },
    #           "latitude": 0,
    #           "longitude": 0,
    #           "name": "شلوار - محصول مرجع",
    #           "categoryList": [],
    #           "unlimited": false,
    #           "availableCount": 764,
    #           "price": 15,
    #           "discount": 0,
    #           "rate": {
    #             "rate": 0,
    #             "rateCount": 0
    #           },
    #           "attributeValues": [],
    #           "guild": {
    #             "id": 52,
    #             "name": "پوشاک",
    #             "code": "CLOTHING_GUILD"
    #           },
    #           "allowUserInvoice": false,
    #           "allowUserPrice": false,
    #           "currency": {
    #             "name": "ریال",
    #             "code": "IRR"
    #           }
    #         },
    #         "amount": 15,
    #         "description": "توضیحی ندارم",
    #         "quantity": 1,
    #         "discount": 0,
    #         "voucherUsageSrvs": []
    #       }
    #     ],
    #     "guildSrv": {
    #       "id": 52,
    #       "name": "پوشاک",
    #       "code": "CLOTHING_GUILD"
    #     },
    #     "userSrv": {
    #       "id": 16849,
    #       "name": "رضا زارع",
    #       "ssoId": "11923337",
    #       "ssoIssuerCode": 1,
    #       "profileImage": "https://core.pod.ir:443/nzh/image/?imageId=..."
    #     },
    #     "cellphoneNumber": "09375334941",
    #     "closed": false,
    #     "verificationNeeded": false,
    #     "safe": false,
    #     "postVoucherEnabled": false,
    #     "referenceNumber": "53133389",
    #     "issuerSrv": {
    #       "id": 16128,
    #       "name": "شرکت رضا زارع",
    #       "ssoId": "11963175",
    #       "ssoIssuerCode": 1,
    #       "profileImage": "https://core.pod.ir:443/nzh/image/?imageId=..."
    #     },
    #     "willBeBlocked": false,
    #     "willBePaid": false,
    #     "unsafeCloseTimeOut": 0,
    #     "subInvoice": false,
    #     "edited": false,
    #     "waiting": false
    #   }
    #  ...
    #  ]
    # Total Invoice : 1304
except APIException as e:
    print("API Exception\nError {}\nReference Number : {}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
