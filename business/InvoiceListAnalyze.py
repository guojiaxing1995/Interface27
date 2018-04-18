# -*- coding:utf-8 -*-
import re

class InvoiceListAnalyze():
    '''解析发票列表'''

    def __init__(self,invoiceListAll):
        self.invoiceListAll = invoiceListAll
        # 增票id字符串
        self.invoiceIds = ''
        # 交通票id字符串
        self.trafficIds = ''

    def get_invoicelist(self):
        '''获得已读和未读列表'''
        notReadInvoiceFrontList = self.invoiceListAll['data']['notReadInvoiceFrontList']
        readInvoiceFrontList = self.invoiceListAll['data']['readInvoiceFrontList']

        return readInvoiceFrontList,notReadInvoiceFrontList

    def get_invoice_id(self,invoiceList):
        '''通过发票列表（已读、未读）获得发票id字符串,返回增值税发票（无错票）id字符串和交通票id字符串'''
        invoiceIdList = []
        trafficIdsList = []
        invoiceIds = ''
        trafficIds = ''
        if invoiceList:
            for invoice in invoiceList:
                if invoice['table_type'] == '0' or invoice['table_type'] is None:
                    if invoice['fplb'] == '0' or invoice['fplb'] == '1':
                        invoiceIdList.append(invoice['invoiceinfo_id'])
                    elif invoice['fplb'] == '2' or invoice['fplb'] == '3':
                        trafficIdsList.append(invoice['invoiceinfo_id'])
        else:
            return invoiceIds, trafficIds

        if invoiceIdList:
            for invoiceId in invoiceIdList:
                invoiceIds = invoiceIds + ',' + invoiceId
            invoiceIds = invoiceIds[1:]
        if trafficIdsList:
            for trafficId in trafficIdsList:
                trafficIds = trafficIds + ',' + trafficId
            trafficIds = trafficIds[1:]

        return invoiceIds, trafficIds

    def split_comma(self,string_):
        '''去除字符串前后逗号'''
        if ',' in string_[0]:
            string_ = string_[1:]
        if string_ != '':
            if ',' in string_[-1]:
                string_ = string_[:-1]

        return string_

    def get_invoiceids_string(self):
        '''获取发票列表中的发票id拼接成字符串，用逗号分隔'''
        readInvoiceFrontList, notReadInvoiceFrontList = self.get_invoicelist()
        invoiceid1, trafficid1 = self.get_invoice_id(notReadInvoiceFrontList)
        invoiceid2, trafficid2 = self.get_invoice_id(readInvoiceFrontList)
        invoiceIds = invoiceid1 + ',' + invoiceid2
        trafficIds = trafficid1 + ',' + trafficid2
        self.invoiceIds = self.split_comma(invoiceIds)
        self.trafficIds = self.split_comma(trafficIds)

        return self.invoiceIds,self.trafficIds


    @staticmethod
    def get_invoiceids_list(ids_sting):
        '''通过发票id字符串获得发票id列表'''
        ids_list = ids_sting.split(',')

        return ids_list

    def get_invoiceids_information(self):
        '''
                该方法用于通过发票id获得每一个发票的详细信息
                 通过发票id获得发票tabletype,生成新的列表[{invoiceinfo_id:' ',table_type:' ',......}{invoiceinfo_id:' ',table_type:' ',......},.....]
                 table_type参数唯一标识错票或是对票,错票为1,对票为0,删除发票时需传入该参数
                '''
        invoicesinfor = []
        trafficsinfor = []







