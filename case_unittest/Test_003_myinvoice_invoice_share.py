#encoding=utf-8
import requests
import unittest
from config import config
from util.opreation_gloabal_var import OpreationGloabalVar as globalvar
import random
import re

class myinvoice_invoice_share(unittest.TestCase):
    '''项目名 myinvoice_invoice  发票批量分享相关'''

    def setUp(self):
        self.url = config.GLOBAL_URL + "/myinvoice-invoice/"  # 测试的接口url

    def test_001_ShareInvoiceToPhone(self):
        u"""手机号批量分享"""
        params = {
            "token": globalvar.get_value('token'),
            "random": random.randint(0, 99999999),
            "invoiceIds": globalvar.get_value('invoiceIds'),
            "trafficIds": globalvar.get_value('trafficIds'),
            "phone":"15234093915",
            "clientType":"2"
        }
        url = self.url + 'secured/batchShareInvoice/ShareInvoiceToPhone'
        r = requests.post(url, data=params)
        self.assertEqual(r.status_code, 200)
        response = r.json()
        #self.assertEqual(response['code'], '0000')
        print(r.json())
        print(r.status_code)


    def test_002_getShareRedisKey(self):
        u"""二维码批量分享"""
        params = {
            "token": globalvar.get_value('token'),
            "random": random.randint(0, 99999999),
            "invoiceIds": globalvar.get_value('invoiceIds'),
            "trafficIds": globalvar.get_value('trafficIds'),
            "clientType":"2"
        }
        url = self.url + 'secured/batchShareInvoice/getShareRedisKey'
        r = requests.post(url, params=params)
        self.assertEqual(r.status_code, 200)
        response = r.json()
        global savekey
        savekey = ("".join(re.findall('=.*$',response['data'])))[1:]
        print(savekey)
        print(r.json())
        print(r.status_code)


    def test_003_saveShareInvoice(self):
        u"""接收二维码批量分享发票"""
        params = {
            "token": globalvar.get_value('token'),
            "saveKey": savekey,
            "clientType":"2",
            "random": random.randint(0, 99999999),
        }
        url = self.url + 'secured/batchShareInvoice/saveShareInvoice'
        r = requests.post(url, params=params)
        self.assertEqual(r.status_code, 200)
        print(r.json())
        print(r.status_code)


    def test_004_getBatchShareList(self):
        u"""获取批量分享历史记录"""
        params = {
            "token": globalvar.get_value('token'),
            "random": random.randint(0, 99999999),
            "page": "1",
            "limit":"10",
            "clientType":"2"
        }
        url = self.url + 'secured/batchShareInvoice/getBatchShareList'
        r = requests.post(url, params=params)
        self.assertEqual(r.status_code, 200)
        print(r.json())
        print(r.status_code)



    def test_005_nextShareInvoice(self):
        u"""再次批量分享"""
        params = {
            "token": globalvar.get_value('token'),
            "random": random.randint(0, 99999999),
            "invoiceIds": globalvar.get_value('invoiceIds'),
            "trafficIds": globalvar.get_value('trafficIds'),
            "clientType":"2"
        }
        url = self.url + 'secured/batchShareInvoice/getShareRedisKey'
        r = requests.post(url, params=params)
        self.assertEqual(r.status_code, 200)
        print(r.json())
        print(r.status_code)


    def test_006_getShareAccountForme(self):
        u"""与我分享用户列表      (九期废弃)"""
        data = {
            "token": globalvar.get_value('token')
        }
        url = self.url + 'secured/invoice/getShareAccountForme'
        r = requests.post(url=url,data=data)
        self.assertEqual(r.status_code, 200)
        response = r.json()
        self.assertEqual(response['code'],'0000')
        print(r.json())

    def test_007_shareHistory(self):
        """分享历史接口"""
        data = {
            "token": globalvar.get_value('token')
        }
        url = self.url + 'secured/invoice/shareHistory'
        r = requests.post(url=url, data=data)
        self.assertEqual(r.status_code, 200)
        response = r.json()
        self.assertEqual(response['code'], '0000')

    def test_008_shereFromMe(self):
        """与我分享接口"""
        data = {
            "token": globalvar.get_value('token')
        }
        url = self.url + 'secured/invoice/shereFromMe'
        r = requests.post(url=url, data=data)
        self.assertEqual(r.status_code, 200)
        response = r.json()
        self.assertEqual(response['code'], '0000')

    def test_009_getShareInvoiceList(self):
        """获取分享发票接口"""
        data = {
            "token": globalvar.get_value('token'),
            "shareUid":"",
            "type":""
        }
        url = self.url + 'secured/invoice/getShareInvoiceList'
        r = requests.post(url=url, data=data)
        self.assertEqual(r.status_code, 200)
        response = r.json()
        self.assertEqual(response['code'], '0000')

    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()