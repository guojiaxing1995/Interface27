#encoding=utf-8
import requests
import unittest
from config import config
from util.opreation_gloabal_var import OpreationGloabalVar
from business.InvoiceListAnalyze import InvoiceListAnalyze

class myinvoice_invoice_collect(unittest.TestCase):

    def setUp(self):
        self.url=config.GLOBAL_URL+"/XXXXXXX/"   #测试的接口url

    def test_001_invoice_qrcheck(self):
        for invoice in config.GLOBAL_INVOICE_LIST:
            params={
        "flag": "1",
         "token": OpreationGloabalVar.get_value('token'),
        "infoStr": invoice,
        #"infoStr": {",,031001600411,12357700,,,,"},
        "uuid":"",
        "clientType":"2"
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
                "flag": "1",
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
            "cxrq":"",
            "fplb":"",
            "checkStatus": "",
            "todo":"",
            "xfmc":"",
            "userSettingType":""
            }
        headers = {
            "version":"v1.0.7"
        }
        url = self.url + 'XXXXXXX'
        r = requests.post(url, data=params,headers = headers)
        self.assertEqual(r.status_code, 200)
        #通过解析发票列表获取增票id字符串和交通票id字符串
        invoice_Analyze = InvoiceListAnalyze(r.json())
        invoiceIds,trafficIds = invoice_Analyze.get_invoiceids_string()
        #将得到的字符串设为全局变量
        OpreationGloabalVar.set_value('invoiceIds',invoiceIds)
        OpreationGloabalVar.set_value('trafficIds',trafficIds)


    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()