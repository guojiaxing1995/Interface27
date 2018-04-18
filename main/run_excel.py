#coding:utf-8
from case_excel.get_execel_data import GetData
from execute_one_case import Execute
from util.opreation_email import OpreationEmail


class Run:
    def __init__(self):
        self.data = GetData()
        self.case_run_list = []
        self.pass_list = []
        self.fail_list = []
        # 用例id 与 i 的对应关系
        self.case_i_dict = {}
        #已经执行过的用例集合
        self.has_run_list = []


    def go_on_run(self):
        #用例行数
        lines = self.data.get_case_lines()


        for i in range(2,lines):
            self.data.set_actual_result(i, '')
            self.data.set_interface_return(i,'')
            case_id = self.data.get_case_id(i)
            self.case_i_dict[case_id] = i

        execute_case = Execute()
        case_list = execute_case.execute_method()
        if case_list[0]=='':
            #循环执行全部用例
            for i in range(2,lines):
                execute_case.execute_one_case(i,self.pass_list,self.fail_list,self.case_run_list,self.case_i_dict,self.has_run_list)
        else:
            #执行指定用例
            for y in case_list:
                execute_case.execute_one_case(self.case_i_dict[y], self.pass_list, self.fail_list, self.case_run_list, self.case_i_dict,self.has_run_list,True)

        #将测试结果发送报告
        opreaemail = OpreationEmail()
        receivers = ['3398715569@qq.com', '15234093915@163.com']
        subject = '自动化测试报告'
        content = '用例总数'+str(lines-2)+'条,执行'+str(len(self.case_run_list))+'条,通过'+str(len(self.pass_list))+\
                  '条,失败'+str(len(self.fail_list))+'条'+'\n'+'通过率为 '+str(len(self.pass_list)*100/len(self.case_run_list))+'%'
        opreaemail.SMTP_QQ_send_email(receivers,subject,content,'plain','../case_excel/case.xls')


if __name__ == '__main__':
    run = Run()
    run.go_on_run()



