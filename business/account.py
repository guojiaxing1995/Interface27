# -*- coding:utf-8 -*-
import random,base64

class Account():
    '''用户信息类'''

    def __init__(self,loginresponse):
        self.loginresponse = loginresponse
        self.head_img_url = ''
        self.token = ''
        self.uid = ''

    def get_logininfor(self):
        '''传入登录返回数据,获得token uid 等数据'''
        getdata = self.loginresponse['data']
        self.token = getdata['token']
        self.uid = getdata['uid']

        return self.token,self.uid

    def get_user_headimgurl(self,userinforresponse):
        '''传入当前用户信息返会数据,获取head_img_url,head_img_url是获取用户头像接口参数'''
        self.head_img_url = userinforresponse['data']['userInfo']['head_img_url']

        return self.head_img_url

    @staticmethod
    def Unicode():
        '''随机生成汉字  unicode码'''
        str = ''
        for i in range(5):
            val = random.randint(0x4e00, 0x9fbf)
            val = chr(val)
            str = str + val
        return str

    # @staticmethod
    # def GBK2312():
    #     '''随机生成汉字 GB2312码'''
    #     str = ''
    #     for i in range(15):
    #         head = random.randint(0xb0, 0xf7)
    #         body = random.randint(0xa1, 0xfe)
    #         val = f'{head:x}{body:x}'
    #         val = bytes.fromhex(val).decode('gb2312')
    #         str = str + val
    #     return str

    @staticmethod
    def get_img_base64():
        #图片转base64
        f = open(r'method/e.png','rb')
        base64_str = base64.b64encode(f.read())
        f.close()
        base64_str = base64_str.decode('utf-8')
        return  base64_str







