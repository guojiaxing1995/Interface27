import json
import re
import time

from base.runmethod import RunMethod
from case_excel.get_execel_data import GetData
from util.opreation_excel import OperationExcel
from util.opreation_gloabal_var import OpreationGloabalVar


class Execute:

    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.excel = OperationExcel('../case_excel/case.xlsx')

    # 得到执行方式，全部执行还是执行哪几条
    def execute_method(self):
        self.excel.get_table(sheet_name='case1')
        case_string = self.excel.get_cell_value(1, 12)
        case_list = re.findall(':(.*)', case_string)
        if case_list:
            case_list = case_list[0].split(',')
        return case_list

    # 获取参数数据,转换成对应格式
    def data_deal(self, data, json_str, header):
        if data:
            data = json.loads(data)
        if json_str:
            json_str = json.loads(json_str)
        if header:
            header = json.loads(header)

        return data, json_str, header

    # 接口返回数据的处理
    def response_deal(self, deal_method, res, process_statement):
        if deal_method:
            if 'deal_default' in deal_method:
                if re.findall('\((.*)\)', deal_method)[0].split(',') == ['']:
                    OGV = OpreationGloabalVar({})
                    OpreationGloabalVar.push_global_dict(OGV.deal_data(res.json()))
                else:
                    OGV = OpreationGloabalVar({})
                    dict = OGV.deal_data(res.json(), None, re.findall('\((.*)\)', deal_method)[0].split(','))
                    OpreationGloabalVar.push_global_dict(dict)
                self.default_process_statement(process_statement, OpreationGloabalVar.get_global_dict())
            else:
                self.get_function(deal_method, res.json())

    def get_function(self, method_name, data):
        fun = globals().get(method_name)
        fun(data)

    # 默认处理的 辅助处理语句  将全局变量字典中的key换成指定key  key,new_key key,new_key
    def default_process_statement(self, process_statement, var_dick):
        if process_statement:
            key_items = process_statement.split()
            for key_item in key_items:
                oid_key = key_item.split(',')[0]
                new_key = key_item.split(',')[1]
                if oid_key in var_dick.keys():
                    var_dick[new_key] = var_dick[oid_key]
                    var_dick.pop(oid_key)

    # 判断用例执行是否通过,将返回结果写回excel表格
    def deal_result(self, res, expend_result, i, case_id, pass_list, fail_list):
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

    # 将入参、header、url 中的变量替换为数据
    def var_substitution(self, url, header, data, json_str, var_dick):
        # url 处理
        url_var = re.search(r'\${(.*)\}', url)
        if url_var:
            try:
                var = var_dick[url_var.group(1)]
            except Exception:
                # 如果变量不在全局字典中则赋值变量为 ''
                var = ''
            url = url.replace(url_var.group(0), str(var))

        # header 处理
        if header:
            for key, value in header.items():
                if type(value) == str:
                    header_var = re.search(r'\${(.*)\}', value)
                    if header_var:
                        try:
                            header[key] = var_dick[header_var.group(1)]
                        except Exception:
                            # 如果变量不在全局字典中则赋值变量为 None
                            header[key] = None

        # data 处理
        if data:
            for key, value in data.items():
                if type(value) == str:
                    data_var = re.search(r'\${(.*)\}', value)
                    if data_var:
                        try:
                            data[key] = var_dick[data_var.group(1)]
                        except Exception:
                            # 如果变量不在全局字典中则赋值变量为 None
                            data[key] = None
                # 处理value为列表的情况
                if type(value) == list:
                    for i in range(len(value)):
                        if type(value[i]) == str:
                            data_var = re.search(r'\${(.*)\}', value[i])
                            if data_var:
                                try:
                                    data[key][i] = var_dick[data_var.group(1)]
                                except Exception:
                                    # 如果变量不在全局字典中则赋值变量为 None
                                    data[key][i] = None
                # 处理value为字典的情况
                if type(value) == dict:
                    for key_second, value_second in value.items():
                        if type(value_second) == str:
                            data_var = re.search(r'\${(.*)\}', value_second)
                            if data_var:
                                try:
                                    data[key][key_second] = var_dick[data_var.group(1)]
                                except Exception:
                                    # 如果变量不在全局字典中则赋值变量为 None
                                    data[key][key_second] = None

        # json_str 处理
        if json_str:
            for key, value in json_str.items():
                if type(value) == str:
                    data_var = re.search(r'\${(.*)\}', value)
                    if data_var:
                        try:
                            json_str[key] = var_dick[data_var.group(1)]
                        except Exception:
                            # 如果变量不在全局字典中则赋值变量为 None
                            json_str[key] = None
                # 处理value为列表的情况
                if type(value) == list:
                    for i in range(len(value)):
                        if type(value[i]) == str:
                            data_var = re.search(r'\${(.*)\}', value[i])
                            if data_var:
                                try:
                                    json_str[key][i] = var_dick[data_var.group(1)]
                                except Exception:
                                    # 如果变量不在全局字典中则赋值变量为 None
                                    json_str[key][i] = None
                # 处理value为字典的情况
                if type(value) == dict:
                    for key_second, value_second in value.items():
                        if type(value_second) == str:
                            data_var = re.search(r'\${(.*)\}', value_second)
                            if data_var:
                                try:
                                    json_str[key][key_second] = var_dick[data_var.group(1)]
                                except Exception:
                                    # 如果变量不在全局字典中则赋值变量为 None
                                    json_str[key][key_second] = None

        return url, header, data, json_str

    # 执行一条测试用例
    def execute_one_case(self, i, pass_list, fail_list, case_run_list, case_i_dict, has_run_list, must_flag=False):
        # 判断依赖用例是否已经执行，若未执行则强制执行
        depend_caseid = self.data.get_depend_caseid(i)
        if depend_caseid:
            depend_list = depend_caseid.split(',')
            for x in depend_list:
                if x not in has_run_list:
                    self.execute_one_case(case_i_dict[x], pass_list, fail_list, case_run_list, case_i_dict,
                                          has_run_list, True)
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
            process_statement = self.data.get_process_statement(i)
            expend_result = self.data.get_expend_result(i)
            header = self.data.get_header(i)

            case_run_list.append(case_id)

            # 数据格式转化
            data, json_str, header = self.data_deal(data, json_str, header)
            # 替换变量为数据
            url, header, data, json_str = self.var_substitution(url, header, data, json_str,
                                                                OpreationGloabalVar.get_global_dict())
            res = self.run_method.run_main(method, url, header, data, json_str)
            has_run_list.append(case_id)
            # 处理接口返回数据
            self.response_deal(deal_method, res, process_statement)
            # 用例执行结果记录
            self.deal_result(res, expend_result, i, case_id, pass_list, fail_list)
            actual_result = self.data.get_actual_result(i)
