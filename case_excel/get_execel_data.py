from openpyxl.styles import Font

from case_excel.excel_column import excel_column
from config.config import *
from util.opreation_excel import OperationExcel


class GetData:
    def __init__(self):
        self.excel = OperationExcel()
        self.table = self.excel.get_table()

    # 获取用例行数
    def get_case_lines(self):
        lines = self.excel.get_rows()
        return lines

    # 获取用例名称
    def get_case_name(self, row):
        col = excel_column.getcolumn_case_name()
        case_name = self.excel.get_cell_value(row, col)
        return case_name

    # 获取用例di
    def get_case_id(self, row):
        col = excel_column.getcolumn_case_id()
        case_id = self.excel.get_cell_value(row, col)
        return case_id

    # 获取是否执行
    def get_isrun(self, row):
        col = excel_column.getcolumn_isrun()
        run_modul = self.excel.get_cell_value(row, col)
        flag = None
        if run_modul == 'yes' or run_modul == 'YES':
            flag = True
        elif run_modul == 'no' or run_modul == 'NO':
            flag = False
        return flag

    # 获取请求方法
    def get_method(self, row):
        col = excel_column.getcolumn_method()
        request_method = self.excel.get_cell_value(row, col)
        return request_method

    # 获取接口地址
    def get_url(self, row):
        col = excel_column.getcolumn_URL()
        url = self.excel.get_cell_value(row, col)
        if 'http' not in url:
            url = GLOBAL_URL + url
        return url

    # 获取依赖用例id
    def get_depend_caseid(self, row):
        col = excel_column.getcolumn_depend_case()
        depend_caseid = self.excel.get_cell_value(row, col)
        return depend_caseid

    # 获取header
    def get_header(self, row):
        col = excel_column.getcolumn_header()
        header = self.excel.get_cell_value(row, col)
        return header

    # 获取data请求数据
    def get_data(self, row):
        col = excel_column.getcolumn_data()
        data = self.excel.get_cell_value(row, col)
        return data

    # 获取json请求数据
    def get_json(self, row):
        col = excel_column.getcolumn_json()
        json = self.excel.get_cell_value(row, col)
        return json

    # 获取逾期结果
    def get_expend_result(self, row):
        col = excel_column.getcolumn_expend_result()
        expend_result = self.excel.get_cell_value(row, col)
        return expend_result

    # 获取数据处理方法
    def get_data_deal(self, row):
        col = excel_column.getcolumn_data_deal()
        deal_method = self.excel.get_cell_value(row, col)
        return deal_method

    # 获取依赖数据所属字段
    def get_process_statement(self, row):
        col = excel_column.getcolumn_depend_key()
        depend_key = self.excel.get_cell_value(row, col)
        return depend_key

    # 写入实际结果
    def set_actual_result(self, row, value):
        col = excel_column.getcolumn_actual_result()
        font_false = Font(size=12, bold=True, color="FF0000") if value == 'fail' else None
        self.excel.write_execel(row, col, value, font_false)

    # 写入接口返回数据
    def set_interface_return(self, row, value):
        col = excel_column.getcolumn_interface_return()
        self.excel.write_execel(row, col, value)

    # 获取逾期结果
    def get_actual_result(self, row):
        col = excel_column.getcolumn_actual_result()
        actual_result = self.excel.get_cell_value(row, col)
        return actual_result
