from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


# 打开Chrome浏览器
driver = webdriver.Chrome()

# 进入百度高级搜索页
url = "https://www.baidu.com/"

driver.get(url)
driver.maximize_window()

driver.find_element(By.ID,'kw').send_keys('NBA')
driver.find_element(By.ID,'su').click()
sleep(3)


#拖动该页面的滚动条
js_sentence_position = "document.documentElement.scrollTop=9999"
driver.execute_script(js_sentence_position)



#点击登录Button
# driver.find_element(By.ID,'s-top-loginbtn').click()


#输入账号,密码
# driver.find_element(By.ID,'TANGRAM__PSP_11__userName').send_keys(userName)
# driver.find_element(By.ID,'TANGRAM__PSP_11__password').send_keys(pwd)
# driver.find_element(By.ID,'TANGRAM__PSP_11__submit').click()


# 返回一组字典，对应于当前会话中可见的cookie。
# all_Cookies = driver.get_cookies()
# print(all_Cookies)
#
#
# #返回一组字典，对应于当前会话中可见的cookie。
# driver.delete_cookie('BD_HOME')
#
#
# #返回一组字典，对应于当前会话中可见的cookie。
# cookie_Name = driver.get_cookie('BD_HOME')
# print(cookie_Name)
#
#
# a = {{"name":"name","value":"mouse"}}
# driver.add_cookie(a)

