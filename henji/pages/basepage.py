#!usr/bin/python3.8
#coding=utf-8
from selenium import webdriver
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from test_case.models.Find_element import FindElement

class page(object):
  '''基础页面类，所有的页面类都继承基础页面类'''
  def __init__(self,driver,url):
    self.driver = driver
    self.url = url
    self.timeout = 30
    self.findele = FindElement(driver)

  def _open(self):
    self.driver.get(self.url)
    self.driver.implicitly_wait(5)
    assert self.on_page(),'Did not land on %s' % url

  def find_element(self,key):
    return self.findele.find_element(key)

  def find_elements(self,key):
    return self.findele.find_elements(key)

  def open(self):
    self._open()

  def on_page(self):
    return self.driver.current_url == self.url