#coding:utf8

import smtplib
from email.mime.text import MIMEText
from email.header import Header


mail_host = "smtp.exmail.qq.com"
mail_user = ""
mail_pass = ""

sender = ''
receivers = ['761846158@qq.com']


mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">这是一个链接</a></p>
"""

message = MIMEText(mail_msg,'html','utf-8')

message['From'] = Header('菜鸟测试','utf-8')
message['To'] = Header('测试','utf-8')

subject = "这是测试内容"

message['Subject'] = Header(subject,'utf-8')

try:
	smtpObj = smtplib.SMTP_SSL(mail_host,465)
	smtpObj.login(mail_user,mail_pass)
	smtpObj.sendmail(sender,receivers,message.as_string())
	print("邮件发送成功")
except Exception as e:
	print("Error:无法发送邮件:%s" %e)

