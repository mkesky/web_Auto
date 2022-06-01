from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

#访问地址
url = "http://www.w3school.com.cn/tiy/t.asp?f=jseg_prompt"
url_BaiDu = "https://www.baidu.com/"
driver.get(url_BaiDu)
driver.maximize_window()
driver.implicitly_wait(10)

# #定位alert所在位置元素
driver.switch_to.frame('iframeResult')
# ele = driver.find_element(By.CSS_SELECTOR,'[type="button"]')
# ele.click()
#
# #定位到alert弹窗
# ele_Alert = driver.switch_to.alert
# sleep(5)
#
# #取消弹窗操作
# # ele_Alert.dismiss()
#
# #接受弹窗操作
# # ele_Alert.accept()
#
# #获取弹窗内的文本
# # print(ele_Alert.text)
#
# #向弹窗内的输入数据
# ele_Alert.send_keys("NBA")  #此时并不会在页面展示所传数据,但最终会接受这个数据进行操作
# sleep(3)
#
# ele_Alert.accept()



# 点击登录按钮
driver.find_element(By.LINK_TEXT,'登录').click()
sleep(2)
# 定位登录弹窗的输入框，并输入数据
name_box = driver.find_element(By.NAME,'userName')
name_box.send_keys("Blue")

