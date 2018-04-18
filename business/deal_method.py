#coding:utf-8
from account import Account
from util.opreation_gloabal_var import OpreationGloabalVar as globalvar

def deal_login_data(data):
    account = Account(data)
    token,uid = account.get_logininfor()
    globalvar.set_value('token',token)
    globalvar.set_value('uid',uid)

def get_function(method_name,data):
    fun = globals().get(method_name)
    fun(data)

