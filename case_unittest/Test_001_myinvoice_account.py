#encoding=utf-8
import requests
import unittest
from business.account import Account
from config import config
from util.opreation_gloabal_var import OpreationGloabalVar

class Myinvoice_account(unittest.TestCase):
    u"""项目名myinvoice-account"""
    def setUp(self):
        self.url=config.GLOBAL_URL+"/myinvoice-account/"   #测试的接口url


    def test_001_login(self):
        u"""手机号登录"""
        params=config.GLOBAL_USER_INFO
        url = self.url+'account/app/login'
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
        '''获取当前用户的个人资料'''
        datas = {
            "token": OpreationGloabalVar.get_value('token'),
            "uid": OpreationGloabalVar.get_value('uid'),
        }
        url = self.url + 'account/user/getUserInfo'
        r = requests.post(url=url,data=datas)
        self.assertEqual(r.status_code, 200)
        response = r.json()
        self.assertEqual(response['code'],'0000')
        account.get_user_headimgurl(response)

    def test_003_updateUserInfo(self):
        '''修改当前用户个人信息'''
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
        url = self.url + 'account/user/updateUserInfo'
        r = requests.post(url=url,headers = headers,json=datas,params=params)
        self.assertEqual(r.status_code,200)
        response = r.json()
        self.assertEqual(response['code'],'0000')
        print(r.json())


    def test_004_downloadImg(self):
        '''获取下载用户头像'''
        url = self.url + 'account/user/downloadImg/' + OpreationGloabalVar.get_value('head_img_url')
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