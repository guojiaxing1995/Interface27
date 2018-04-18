#coding:utf-8
import unittest,time,os
import HTMLTestRunnerCN
from util.opreation_email import OpreationEmail

class Run():

    def __init__(self):
        pass

    def creatsuit(self):
        testunit = unittest.TestSuite()
        #测试文件查找的目录
        test_dir = '../case_unittest'
        #discover方法筛选Test开头的文件
        discover = unittest.defaultTestLoader.discover(test_dir, pattern='Test_*.py', top_level_dir=None)
        #将筛选出来的用例,循环添加套件
        for test_suit in discover:
            for test_case in test_suit:
                testunit.addTest(test_case)
                print(testunit)

        return testunit

    def run_case_creat_report(self,title=u'接口自动化',description=u'用例执行情况:',tester=u'自动化测试团队'):
        # 获取当前时间
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        # 定义报告存放路径,确保此路径已存在
        filename = '../report/' + now + 'result.html'
        fp = open(filename, 'wb')
        # 设定测试报告相关信息
        runner = HTMLTestRunnerCN.HTMLTestRunner(
            stream=fp,
            title=title,
            description=description,
            tester=tester
        )

        runner.run(self.creatsuit())
        # 关闭报告文件
        fp.close()

    #选择最新的报告
    def new_report(self,testreport):
        lists = os.listdir(testreport)
        lists.sort(key=lambda fn: os.path.getatime(testreport + "\\" + fn))
        file_new = os.path.join(testreport, lists[-1])
        print (file_new)
        return file_new

if __name__=='__main__':
    run = Run()
    opreaemail = OpreationEmail()
    #run.run_case_creat_report()
    new_report = run.new_report('../report/')

    receivers = ['3398715569@qq.com', '15234093915@163.com']
    subject = '自动化测试报告'
    content = '自动化测试报告'
    opreaemail.SMTP_QQ_send_email(receivers, subject, open(new_report, 'rb').read(), 'html', new_report)