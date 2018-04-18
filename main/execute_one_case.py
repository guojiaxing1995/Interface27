#coding:utf-8
from base.runmethod import RunMethod
from case_excel.get_execel_data import GetData
from business.deal_method import get_function
from util.opreation_gloabal_var import OpreationGloabalVar
from util.opreation_excel import OperationExcel
from util.opreation_mysql import OperationMysql
import json
import re,time

class Execute():

    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()

    #得到执行方式，全部执行还是执行哪几条
    def execute_method(self):
        excel = OperationExcel('../case_excel/case.xls')
        table = excel.get_table(excel.workbook, sheet_name='case1', sheet_id=0)
        case_string = excel.get_cell_value(table, 0, 11)
        case_list = re.findall(':(.*)',case_string)
        if case_list!=[]:
            case_list = case_list[0].split(',')
        return case_list

    #获取参数数据,转换成对应格式
    def data_deal(self,data,json_str,header):
        if data:
            data = json.loads(data)
        if json_str:
            json_str = json.loads(json_str)
        if header:
            header = json.loads(header)

        return data,json_str,header

    #获取依赖参数,将依赖参数填入参数字典中
    def get_depend_key(self,depend_key,data,json_str):
        if depend_key:
            list_depend = depend_key.split()
            list_data = list_depend[0].split(',')
            for data_depend in list_data:
                data[data_depend] = OpreationGloabalVar.get_value(data_depend)
            if len(list_depend) > 1 and json_str:
                for json_depend in list_depend[1].split(','):
                    json_str[json_depend] = OpreationGloabalVar.get_value(json_depend)

    #接口返回数据的处理
    def response_deal(self,deal_method,res):
        if deal_method:
            if 'deal_default' in deal_method:
                if re.findall('\((.*)\)', deal_method)[0].split(',') == ['']:
                    OGV = OpreationGloabalVar({})
                    OpreationGloabalVar.push_global_dict(OGV.deal_data(res.json()))
                else:
                    OGV = OpreationGloabalVar({})
                    dict = OGV.deal_data(res.json(), None, re.findall('\((.*)\)', deal_method)[0].split(','))
                    OpreationGloabalVar.push_global_dict(dict)
            else:
                get_function(deal_method, res.json())

    #判断用例执行是否通过,将返回结果写回excel表格
    def deal_result(self,res,expend_result,i,case_id,pass_list,fail_list):
        if res.status_code == 200:
            if expend_result in res.text:
                self.data.set_actual_result(i, 'pass')
                pass_list.append(case_id)
            else:
                self.data.set_actual_result(i, 'fail')
                fail_list.append(case_id)
        else:
            self.data.set_actual_result(i, 'fail')
            fail_list.append(case_id)
        self.data.set_interface_return(i, res.text)

    #执行纪律插入数据库
    def case_inset(self,case_id,case_name,is_run,method,url,header,deal_method,depend_id,depend_postion,data_str,json_str,expect_result,actusl_result,interface_return,deal_time):
        opmysql = OperationMysql('wdfp')
        sql = 'INSERT INTO WDFP_CASE VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' % (case_id,case_name,is_run,method,url,header,deal_method,depend_id,depend_postion,data_str,json_str,expect_result,actusl_result,interface_return,deal_time)
        opmysql.insert(sql)

    #执行一条测试用例
    def execute_one_case(self,i,pass_list,fail_list,case_run_list,case_i_dict,has_run_list,must_flag=False):
        # 判断依赖用例是否已经执行，若未执行则强制执行
        depend_caseid = self.data.get_depend_caseid(i)
        if depend_caseid:
            depend_list = depend_caseid.split(',')
            for x in depend_list:
                if x not in has_run_list:
                    self.execute_one_case(case_i_dict[x],pass_list,fail_list,case_run_list,case_i_dict,has_run_list,True)
                    has_run_list.append(x)

        is_run = self.data.get_isrun(i)
        if must_flag is True:
            is_run = True
        if is_run:
            case_id = self.data.get_case_id(i)
            case_name = self.data.get_case_name(i)
            method = self.data.get_method(i)
            url = self.data.get_url(i)
            data = self.data.get_data(i)
            json_str = self.data.get_json(i)
            deal_method = self.data.get_data_deal(i)
            depend_key = self.data.get_depend_key(i)
            expend_result = self.data.get_expend_result(i)
            header = self.data.get_header(i)

            case_run_list.append(case_id)

            #数据格式转化
            data,json_str,header = self.data_deal(data,json_str,header)
            #如果有依赖参数存在,则获取依赖参数然后填写到对应列表中
            self.get_depend_key(depend_key,data,json_str)
            res = self.run_method.run_main(method, url, header, data, json_str)
            has_run_list.append(case_id)
            #处理接口返回数据
            self.response_deal(deal_method,res)
            #用例执行结果记录
            self.deal_result(res,expend_result,i,case_id,pass_list,fail_list)
            actual_result = self.data.get_actual_result(i)
            #将执行结果存入数据库
            self.case_inset(case_id,case_name,is_run,method,url,header,deal_method,depend_caseid,depend_key,data,json_str,expend_result,actual_result,res.text(),time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))