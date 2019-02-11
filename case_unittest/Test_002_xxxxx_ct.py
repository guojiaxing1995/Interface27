#encoding=utf-8
import requests
import unittest
from config import config
from util.opreation_gloabal_var import OpreationGloabalVar

class myinvoice_invoice_collect(unittest.TestCase):

    def setUp(self):
        self.url=config.GLOBAL_URL+"/XXXXXXX/"   #测试的接口url

    def test_001_invoice_qrcheck(self):
        for invoice in config.GLOBAL_INVOICE_LIST:
            params={
        "flag": "1",
         "token": OpreationGloabalVar.get_value('token'),
        #"infoStr": {",,031001600411,12357700,,,,"},
        "uuid":"",
                    }
            url = self.url+'XXXXXXXXX'
            r = requests.post(url, params=params)
            self.assertEqual(r.status_code, 200)
            res = r.json()
            self.assertEqual(res['code'], '0000')
            print(r.json())

    def test_002_invoice_ocr_trafficInvoiceCollection(self):
        for traffic in config.GLOBAL_TRAFFIC_LIST:
            params = {
                "token": OpreationGloabalVar.get_value('token')
                }
            headers = {
                'Accept': "Application/json",
                'Content-Type': "application/json"
            }
            #payload = "{\r\n\"invoice_type\": \"3\",\r\n\"je\": \"35.00\",\r\n\"kprq\": \"2017-09-15 08:20:30\",\r\n\"name\": \"dachepiao\",\r\n\"train_time\": \"2017-09-15 08:20:30\",\r\n\"uuid\": \"\"\r\n}"
            payload = traffic
            url = self.url + 'XXXXXXXXX'
            r = requests.post(url, params=params,headers=headers,json=payload)
            self.assertEqual(r.status_code, 200)
            res = r.json()
            self.assertEqual(res['code'], '0000')
            print(r.json())

    def test_003_invoice_getInvoiceList(self):
        params = {
            "token": OpreationGloabalVar.get_value('token'),

            }
        headers = {

        }
        url = self.url + 'XXXXXXX'
        r = requests.post(url, data=params,headers = headers)
        self.assertEqual(r.status_code, 200)
        invoice_Analyze = InvoiceListAnalyze(r.json())
        invoiceIds,trafficIds = invoice_Analyze.get_invoiceids_string()
        OpreationGloabalVar.set_value('invoiceIds',invoiceIds)
        OpreationGloabalVar.set_value('trafficIds',trafficIds)


    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()