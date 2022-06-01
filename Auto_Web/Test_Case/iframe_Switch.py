from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

#访问地址
url = "https://mail.qq.com/"
account = "BlueSky@163.com"
pwd = "123456"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)

driver.switch_to.frame(1)
time.sleep(2)
driver.find_element(By.ID,'u').send_keys(account)
time.sleep(2)
driver.find_element(By.ID,'p').send_keys(pwd)
time.sleep(2)
driver.find_element(By.ID,'login_button').click()



