#encoding=utf-8
import requests
import unittest
from config import config
from util.opreation_gloabal_var import OpreationGloabalVar as globalvar
import random

class myinvoice_invoice(unittest.TestCase):
    def setUp(self):
        self.url=config.GLOBAL_URL+"/XXXXX/"   #测试的接口url


    def test_001_getTodoLabelList(self):
        u"""获取批量待办信息"""
        params={
      "token": globalvar.get_value('token'),
      "random": random.randint(0, 99999999),
      "invoiceIds": globalvar.get_value('invoiceIds'),
      "trafficIds": globalvar.get_value('trafficIds')
}
        url = self.url+'XXXXX'
        r = requests.post(url, params=params)

        self.assertEqual(r.status_code, 200)
        print(r.json())

    def test_002_saveBatchTodoLabels(self):
        params = {
            "token": globalvar.get_value('token'),
            "random": random.randint(0, 99999999),
            "todoLabels":"报销",
            "invoiceIds": globalvar.get_value('invoiceIds'),
            "trafficIds": globalvar.get_value('trafficIds')
        }
        url = self.url + 'XXXXX'
        r = requests.post(url, data=params)

        self.assertEqual(r.status_code, 200)
        #print(r.json())

    def test_003_getLabels(self):
        data = {
            "token": globalvar.get_value('token')
        }
        url = self.url + 'XXXXXX'
        r = requests.post(url, data=data)
        self.assertEqual(r.status_code,200)
        response = r.json()
        self.assertEqual(response['code'], '0000')
        print(response)

    def test_004_saveCategoryBatch(self):
        params = {
            "token": globalvar.get_value('token'),
            "random": random.randint(0, 99999999),
            "categoryLabels":"交通|数码",
            "invoiceIds": globalvar.get_value('invoiceIds'),
            "trafficIds": globalvar.get_value('trafficIds')
        }
        url = self.url + 'XXXXXXXXX'
        r = requests.post(url, data=params)
        self.assertEqual(r.status_code, 200)
        response = r.json()
        print(response)

    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()