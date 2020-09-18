import sys
#sys.path.append("/home/lee/test_projects/henji/test_case/models")
from models.readini import ReadIni
from selenium import webdriver

class FindElement(object):
  def __init__(self,driver):
    self.driver = driver

  def find_element(self,key):
    readini = ReadIni()
    data = readini.get_value(key)
    by = data.split(":",1)[0]
    value = data.split(":",1)[1]
    try:
      if by == 'id':
        return self.driver.find_element_by_id(value)
      if by == 'name':
        return self.driver.find_element_by_name(value)
      if by == 'css':
        return self.driver.find_element(By.CSS_SELECTOR,value)
      if by == 'xpath':
        return self.driver.find_element_by_xpath(value)
      if by == 'class_name':
        return self.driver.find_element_by_class_name(value)
      if by == 'tag_name':
        return self.driver.find_element_by_tag_name(value)
      if by == 'link_text':
        return self.driver.find_element_by_link_text(value)
    except Exception as e:
        return None

  def find_elements(self,key):
    readini = ReadIni()
    data = readini.get_value(key)
    by = data.split(":",1)[0]
    value = data.split(":",1)[1]
    try:
      if by == 'id':
        return self.driver.find_elements_by_id(value)
      if by == 'name':
        return self.driver.find_elements_by_name(value)
      if by == 'css':
        return self.driver.find_elements_by_css_selector(value)
      if by == 'xpath':
        return self.driver.find_elements_by_xpath(value)
      if by == 'class_name':
        return self.driver.find_elements_by_class_name(value)
      if by == 'tag_name':
        return self.driver.find_elements_by_tag_name(value)
      if by == 'link_text':
        return self.driver.find_elements_by_link_text(value)
    except Exception as e:
      return None        

if __name__ == "__main__":
  FindElement.find_element("text_username")