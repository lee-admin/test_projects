from selenium import webdriver
import os

#截图函数
def save_screenshot(driver,file_name):
  base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
  base_dir = str(base_dir)
  file_path = base_dir + "/report/image/" + file_name
  driver.get_screenshot_as_file(file_path)


if __name__ == '__main__':
  driver = webdriver.Chrome()
  driver.get("https://www.baidu.com")
  save_screenshot(driver, 'test.png')
  driver.quit()