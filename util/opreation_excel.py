#coding:utf-8
import xlrd
from xlutils.copy import copy

class OperationExcel:
    def __init__(self,file_name=None):
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = '../case_excel/case.xls'
        self.workbook = self.get_workbook(self.file_name)

    def get_workbook(self,file_name):
        workbook = xlrd.open_workbook(file_name)
        return workbook

    def get_table(self,workbook,sheet_name=None,sheet_id=0):
        table = workbook.sheets()[sheet_id]
        if sheet_name:
            table = workbook.sheet_by_name(sheet_name)
        return table

    def get_rows(self,table):
        rows = table.nrows
        return rows

    def get_cols(self,table):
        cols = table.ncols
        return cols

    def get_cell_value(self,table,x,y):
        cell_value = table.cell_value(x, y)
        return cell_value

    def write_execel(self,workbook,sheetid,row,col,value):
        workbook_copy = copy(workbook)
        sheet_write = workbook_copy.get_sheet(sheetid)
        sheet_write.write(row,col,value)
        workbook_copy.save(self.file_name)

if __name__ == '__main__':
    excel = OperationExcel('../case_excel/case.xls')
    table = excel.get_table(excel.workbook,sheet_name='case1',sheet_id=0)
    # rows = excel.get_rows(table)
    #excel.write_execel(6,2,'pass')
    #print(rows)

    print(excel.get_cell_value(table,0,11))
