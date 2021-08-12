import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class OpreationEmail():

    # 使用第三方SMTP服务
    def SMTP_QQ_send_email(self, receivers, subject, content, format='plain', attachment_path=None,
                           attachment_name=None):
        mail_host = "smtp.qq.com"
        mail_user = "3398715569@qq.com"
        mail_pass = "zllobcywxyrucibh"

        sender = '3398715569@qq.com'

        message = MIMEMultipart()
        # 邮件主题
        message['subject'] = subject
        message['From'] = '3398715569@qq.com'
        message['To'] = ','.join(receivers)

        # 邮件正文内容
        message.attach(MIMEText(content, format, 'utf-8'))

        if attachment_path:
            # 构造附件
            att1 = MIMEText(open(attachment_path, 'rb').read(), 'base64', 'utf-8')
            att1["Content-Type"] = 'application/octet-stream'
            if attachment_name:
                att1['Content-Disposition'] = 'attachment;filename=' + attachment_name
            else:
                att1['Content-Disposition'] = 'attachment;filename=' + attachment_path.split("/")[-1]
            message.attach(att1)

        smtpOjb = smtplib.SMTP_SSL()
        smtpOjb.connect(mail_host, 465)
        smtpOjb.login(mail_user, mail_pass)
        smtpOjb.sendmail(sender, receivers, message.as_string())
        smtpOjb.close()
        print('邮件发送成功')


if __name__ == '__main__':
    receivers = ['3398715569@qq.com', '15234093915@163.com']
    subject = '测试邮件标题'
    content = '测试报告邮件内容正文'
    opreaemail = OpreationEmail()
    opreaemail.SMTP_QQ_send_email(receivers, subject, content, 'plain', '../case_excel/case.xlsx', '测试报告.xls')
