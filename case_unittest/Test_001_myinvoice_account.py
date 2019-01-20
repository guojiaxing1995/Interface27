#encoding=utf-8
import requests
import unittest
from business.account import Account
from config import config
from util.opreation_gloabal_var import OpreationGloabalVar

class Myinvoice_account(unittest.TestCase):
    def setUp(self):
        self.url=config.GLOBAL_URL+"/XXXXXX/"   #测试的接口url


    def test_001_login(self):
        params=config.GLOBAL_USER_INFO
        url = self.url+'XXXXXX'
        r = requests.post(url=url, params=params)
        self.assertEqual(r.status_code, 200)
        response = r.json()
        self.assertEqual(response['code'],'0000')
        global account
        account = Account(response)
        token,uid= account.get_logininfor()
        #将获得的token uid 设为全局变量
        OpreationGloabalVar.set_value('token',token)
        OpreationGloabalVar.set_value('uid',uid)

    def test_002_getUserInfo(self):
        datas = {
            "token": OpreationGloabalVar.get_value('token'),
            "uid": OpreationGloabalVar.get_value('uid'),
        }
        url = self.url + 'XXXXXX'
        r = requests.post(url=url,data=datas)
        self.assertEqual(r.status_code, 200)
        response = r.json()
        self.assertEqual(response['code'],'0000')
        account.get_user_headimgurl(response)

    def test_003_updateUserInfo(self):
        headers = {
            "Content-Type":"Application/json"
        }
        params={
            "token": OpreationGloabalVar.get_value('token')
        }
        img_base64 = Account.get_img_base64()
        datas = {
            "sex" : "1",
            "nick_name":Account.Unicode(),
            "city" : Account.Unicode(),
            "country":"中国",
            "province":"北京",
            "lable": Account.GBK2312(),
            "uid":OpreationGloabalVar.get_value('uid'),
            "img":img_base64
         }
        url = self.url + 'XXXXXXX'
        r = requests.post(url=url,headers = headers,json=datas,params=params)
        self.assertEqual(r.status_code,200)
        response = r.json()
        self.assertEqual(response['code'],'0000')
        print(r.json())


    def test_004_downloadImg(self):
        url = self.url + 'XXXXXXX/' + OpreationGloabalVar.get_value('head_img_url')
        r = requests.get(url=url,stream=True)
        f = open('a','wb')
        for chunk in r.iter_content(chunk_size=512):
            if chunk:
                f.write(chunk)
        f.close()


    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()