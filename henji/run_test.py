#!usr/bin/python3.8
#coding=utf-8
import unittest
#import test_cases.test_baidu,hengji
from HTMLTestRunner import HTMLTestRunner
import time
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import smtplib
import os

test_dir = './test_case/'
#将test_case文件夹中所有.py文件中的test开头的用例加入测试列表
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*.py')

def send_mail(file_new):
  """测试邮箱为zidonghua2020@163.com,密码：ehigh123"""
  smtpserver = "smtp.163.com"
  sender = "zidonghua_2020@163.com"
  #此处添加收件人
  receivers = ["zidonghua_2020@163.com", ]
  user = "zidonghua_2020@163.com"
  password = "JAOVXSDLCWGFWYSM"
  subject = "自动化测试报告"
  sendfile = open(file_new, 'rb').read()
  mail_body = "查看测试报告请下载附件"

  msgRoot = MIMEMultipart()
  msgRoot['From'] = "{}".format(sender)  
  msgRoot['To'] = ",".join(receivers)    
  msgRoot['Subject'] = subject
  msgtext = MIMEText(mail_body, _subtype='plain', _charset='utf-8')
  msgRoot.attach(msgtext)

  ff = open(file_new, 'rb')
  att = MIMEText(ff.read(), 'base64', 'utf-8')
  # 附件设置内容类型，设置为二进制流
  att["Content-Type"] = 'application/octet-stream'
  # 设置附件头，添加文件名
  att["Content-Disposition"] = 'attachment; filename="test_result.html"'
  # 中文附件名乱码问题
  # att.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', basename))
  msgRoot.attach(att)
  ff.close()

  smtp = smtplib.SMTP()
  smtp.connect(smtpserver)
  smtp.login(user, password)
  smtp.sendmail(sender, receivers, msgRoot.as_string())
  smtp.quit()


def new_report(testreport):
  '''返回最新的测试报告'''
  lists = os.listdir(testreport)
  lists.sort(key=lambda fn: os.path.getmtime(testreport + "/" + fn))
  file_new = os.path.join(testreport, lists[-1])
  return file_new


if __name__ == '__main__':
  now = time.strftime("%Y-%m-%d %H:%M:%S")
  filename = "./report/" + now + "result.html"
  report_file = open(filename,"wb")
  runner = HTMLTestRunner(stream=report_file,title="测试报告",description="用例执行情况")
  runner.run(discover) 
  report_file.close()
  file_path = new_report('./report')
  send_mail(file_path)