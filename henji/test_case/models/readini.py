from configparser import ConfigParser
import os

class ReadIni(object):
  """读取配置文件"""
  def __init__(self,file=None,node=None):
    if file == None:
      file = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) +\
      "/Config/config.ini"
    if node == None:
      self.node = "Loginelements"
      self.cf = ConfigParser()
      self.cf.read(file)

  def get_value(self,key):
    return self.cf.get(self.node,key)


if __name__ == "__main__":
  print(ReadIni.get_value("text_username"))