#!usr/bin/python3.8
#coding=utf-8
import unittest
#import test_cases.test_baidu,hengji
from HTMLTestRunner import HTMLTestRunner
import time

test_dir = './test_case/'
#将test_case文件夹中所有.py文件中的test开头的用例加入测试列表
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*.py')

if __name__ == '__main__':
  now = time.strftime("%Y-%m-%d %H:%M:%S")
  filename = "./report/" + now + "result.html"
  report_file = open(filename,"wb")
  runner = HTMLTestRunner(stream=report_file,title="测试报告",description="用例执行情况")
  runner.run(discover) 
  report_file.close()


