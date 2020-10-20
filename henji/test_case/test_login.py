# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest
from HTMLTestRunner import HTMLTestRunner
from models.myunite import MyTest
import sys
import os
from models.function import save_screenshot
BASE_Dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_Dir)
from pages.loginPage import Loginpage


class TestLogin(MyTest):
  '''login模块测试'''

  def test_loginRidRname(self):
    '''正确用户名正确密码'''
    po = Loginpage(self.driver)
    po.user_login(username='admin',password='admin')
    self.driver.implicitly_wait(5)
    try:
        po.assert_login_successful()
    except:
        save_screenshot(self.driver, "loginRidRname.png")
    time.sleep(2)

  def test_loginRidWpwd(self):
    '''正确用户名错误密码'''   
    po = Loginpage(self.driver)
    po.user_login(username='admin',password='admmin')
    try:
        po.assert_login_error()
    except:
        save_screenshot(self.driver, "RidWpwd.png")
    time.sleep(2)

  def test_loginWidRpwd(self):
    '''错误用户名正确密码'''    
    po = Loginpage(self.driver)
    po.user_login(username='xxxx',password='admin')
    try:
        po.assert_login_error()
    except:
        save_screenshot(self.driver, "WidRpwd.png")
    time.sleep(2)

  def test_loginEidRpwd(self):
    '''空id'''    
    po = Loginpage(self.driver)
    po.user_login(username='',password='admin')
    try:
        po.assert_login_error()
    except:
        save_screenshot(self.driver, "EidRpwd.png")
    time.sleep(2)
  
  def test_loginRidEpwd(self):
    '''空密码'''    
    po = Loginpage(self.driver)
    po.user_login(username='admin',password='')
    try:
        po.assert_login_error()
    except:
        save_screenshot(self.driver, "RidEpwd.png")
    time.sleep(2)

  def test_loginEidEpwd(self):
    '''空id空密码'''    
    po = Loginpage(self.driver)
    po.user_login(username='',password='')
    try:
        po.assert_login_error()
    except:
        save_screenshot(self.driver, "loginEidEpwd.png")
    time.sleep(2)

  def test_login_data(self):
    '''读入数据进行测试'''
    po = Loginpage(self.driver)
    global BASE_Dir
    login_data_filename = BASE_Dir + "/data/login.txt"
    login_file = open(login_data_filename,'r')
    login_data = login_file.readlines()
    login_data_result_filename = BASE_Dir + "/data/login_result.txt"
    login_result = open(login_data_result_filename,'w')
    login_result.write("用户名   密码\n")
    for login_data_split in login_data:
        i = login_data_split.split(",",1)
        po.open()
        po.login_username(i[0])
        po.login_password(i[1])
        time.sleep(1)
        #登陆失败则刷新掉弹出框再继续测试   
        if self.driver.current_url == "http://192.168.0.69/HGMap/example/":
            login_result.write(i[0] + "  " + i[1] + "登陆失败" + "\n")
            self.driver.refresh()
        #登陆成功则回退到登陆界面
        elif self.driver.current_url == "http://192.168.0.69/HGMap/example/realTime2D.html":
            login_result.write(i[0] + "  " + i[1] + "登陆成功" + "\n")
            self.driver.back()
        #time.sleep(2)
        try:
            assert self.driver.current_url == "http://192.168.0.69/HGMap/example/realTime2D.html" or "http://192.168.0.69/HGMap/example/"
        except:
            save_screenshot(self.driver, "login_data.png")

    login_result.close()
    login_file.close()
    

  def test_login_url(self):
    '''防止直接输入url跳过登陆界面测试'''
    self.driver.get("http://192.168.0.69/HGMap/example/realTime2D.html")
    time.sleep(2)
    try:
        assert self.driver.current_url == "http://192.168.0.69/HGMap/example/index.html"
    except:
        save_screenshot(self.driver, "url.png")

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    #将以下用例加入测试序列
    testunit.addTest(TestLogin("test_login_url"))    
    testunit.addTest(TestLogin("test_loginEidEpwd"))
    testunit.addTest(TestLogin("test_loginRidEpwd"))
    testunit.addTest(TestLogin("test_loginEidRpwd"))
    testunit.addTest(TestLogin("test_loginWidRpwd"))
    testunit.addTest(TestLogin("test_loginRidWpwd"))
    testunit.addTest(TestLogin("test_loginRidRname"))  
    testunit.addTest(TestLogin("test_login_data"))
    #生成测试报告  
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    file_name = "../report/report_module/" + now + "login_" + "result.html"
    report_file = open(file_name, 'wb')
    runner = HTMLTestRunner(stream=report_file, title='login模块测试报告', description='用例执行情况:')
    runner.run(testunit)
    report_file.close()