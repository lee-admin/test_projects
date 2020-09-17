from configparser import ConfigParser

class ReadIni(object):
  """读取配置文件"""
  def __init__(self,file=None,node=None):
    if file == None:
      file = "../../config/config.ini"
    if node == None:
      self.node = "Loginelements"
      self.cf = ConfigParser()
      self.cf.read("/home/lee/test_projects/henji/Config/config.ini")

  def get_value(self,key):
    return self.cf.get(self.node,key)


if __name__ == "__main__":
  print(ReadIni.get_value("text_username"))