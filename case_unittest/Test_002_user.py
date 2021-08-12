# encoding=utf-8
import unittest

import requests
from ddt import ddt, data

from config import config
from util.reportOutputTemplate import report_output_template


@ddt
class ParkingLot(unittest.TestCase):
    def setUp(self):
        self.url = config.GLOBAL_URL + "/api/"  # 测试的接口url
        self.headers = {
            "access_token": "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIxMTA1NDQwMSIsImlhdCI6MTYxNzgwNjExMywiaXNzIjoiMTg5Njkx"
                            "MzgxODAiLCJzdWIiOiIyXzE4OTY5MTM4MTgwXzExMDU0NDAxIn0.FQ92MvwfpsuKa8Uz8EFvyaFyiFhQ47O"
                            "bgM8-cZmSDvM",
            "content-type": "application/json;charset=utf-8",
            "User-Agent": "User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, l"
                          "ike Gecko) Chrome/56.0.2924.87 Safari/537.36"
        }

    def test_001_message_list(self):
        """
        获取用户消息列表
        :return:
        """
        params = {
        }
        url = self.url + 'app/v1/message/list?start=1&limit=10'
        r = requests.post(url=url, data=params, headers=self.headers)
        self.assertEqual(r.status_code, 200)
        report_output_template(url, r.json())

    def test_002_berth_list(self):
        """
        泊位提醒列表
        :return:
        """
        params = {
            "current": 1,
            "size": 10
        }
        url = self.url + 'v1/app/berth/list'
        r = requests.post(url=url, json=params, headers=self.headers)
        self.assertEqual(r.status_code, 201)
        report_output_template(url, r.json())

    def test_003_parking_order(self):
        """
        我的订单-停车订单
        :return:
        """
        url = self.url + 'app/v1/order/parking?start=1&limit=10'
        r = requests.post(url=url, headers=self.headers)
        self.assertEqual(r.status_code, 200)
        report_output_template(url, r.json())

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
