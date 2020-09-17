#!usr/bin/python3.8
#coding=utf-8

#from selenium.webdriver import Remote
from selenium import webdriver

#启动浏览器驱动
def browser():
  #host = '127.0.0.1:4444'    #运行主机的端口号
  #dc = {'browserName': 'firefox'}   #制定浏览器
  #driver = Remote(command_executor='http://' + host + '/wb/hub', desired_capabilities=dc)
  driver = webdriver.Firefox()
  return driver


if __name__ == '__main__':
  dr = browser()
  dr.get("http://www.baidu.com")       #debug
  dr.quit()
