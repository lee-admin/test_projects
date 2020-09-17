from basepage import page
from selenium import webdriver

class Loginpage(page):
  '''登陆页面类'''
  def __init__(self,driver,url="http://192.168.0.69/HGMap/example/"):
    page.__init__(self,driver,url)

  login_username_key = "text_username"
  login_password_key = "text_password"
  login_btnlogin_key = "btn_login"
  login_msg_error = "msg_error"

  def login_username(self,username):
    self.find_element(self.login_username_key).clear()
    self.find_element(self.login_username_key).send_keys(username)

  def login_password(self,password):
    self.find_element(self.login_password_key).clear()
    self.find_element(self.login_password_key).send_keys(password)

  def login_btnlogin(self):
    self.find_element(self.login_btnlogin_key).click()

  def assert_login_error(self):
    #elements = self.find_elements(self.login_msg_error)
    assert len(self.find_elements(self.login_msg_error)) > 0

  def assert_login_successful(self):
    assert self.driver.current_url == "http://192.168.0.69/HGMap/example/realTime2D.html"

  #统一登陆入口
  def user_login(self,username='',password=''):
    self.open()
    self.login_username(username)
    self.login_password(password)
    self.login_btnlogin()
    self.driver.implicitly_wait(5)