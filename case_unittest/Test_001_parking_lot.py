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

    def test_001_parking_list(self):
        """
        获取停车场列表
        :return:
        """
        params = {
            "startLat": 30.19934842808338,
            "startLon": 120.19875605232085,
            "endLat": 30.204739571916623,
            "endLon": 120.20499394767916,
            "currentLon": 120.201875,
            "currentLat": 30.202044
        }
        url = self.url + 'v1/app/parking/list?current=1&size=99'
        r = requests.post(url=url, data=params, headers=self.headers)
        self.assertEqual(r.status_code, 200)
        report_output_template(url, r.json())

    @data('hfw8ao', '3j9hto')
    def test_002_parking_detail(self, parking_code):
        """
        获取停车场详情
        :return:
        """
        params = {
            "parkingCode": parking_code
        }
        url = self.url + 'v1/app/parking/detail'
        r = requests.post(url=url, data=params)
        self.assertEqual(r.status_code, 200)
        report_output_template(url, r.json())

    @data('hfw8ao', '3j9hto')
    def test_003_parking_map(self, parking_code):
        """
        获取导航点位
        :return:
        """
        url = self.url + 'v1/app/parking/getMap?parkingCode=' + parking_code
        r = requests.get(url=url, headers=self.headers)
        self.assertEqual(r.status_code, 200)
        report_output_template(url, r.json())

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
