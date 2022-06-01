from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep



# 模拟鼠标操作-鼠标拖动-滑动验证码
driver = webdriver.Chrome()
url = "file:///C:/Testing/Attachment/slider.html"
driver.get(url)
driver.maximize_window()
account = driver.find_element(By.ID,'id_username')
pwd = driver.find_element(By.ID,'id_password')
#写入账号
account.send_keys('admin')

#写入密码
pwd.send_keys('admin')

sleep(3)
# account.send_keys(Keys.CONTROL,'a')
# account.send_keys(Keys.BACK_SPACE)

#进行回车操作
click_Button = driver.find_element(By.CLASS_NAME,'textbox')
click_Button.send_keys(Keys.ENTER)









# # 获取[滑动条]slider的size
# slider = driver.find_element(By.XPATH,"//*[@id='box']/div[2]")
# slider_size = slider.size
# print(slider_size)
#
# # 获取[滑块]的位置  .location方法获取元素坐标位置,结果一般为：{'x': 200, 'y': 221}这种形式。
# button = driver.find_element(By.XPATH,"//*[@id='box']/div[3]/i")
# button_location = button.location
# print(button_location)
#
# # 拖动操作：drag_and_drop_by_offset
# # 将滑块的位置由初始位置，右移一个滑动条长度（即为x坐标在滑块位置基础上，加上滑动条的长度，y坐标保持滑块的坐标位置）
# x_location = button_location["x"] + slider_size["width"]
# y_location = button_location["y"]
# ActionChains(driver).drag_and_drop_by_offset(button, 500, y_location).perform()



#打开浏览器
# driver = webdriver.Chrome()
# url = "https://www.baidu.com/"
# driver.get(url)
# driver.maximize_window()

#找到需要操作的定位元素
# ele = driver.find_element(By.ID,'kw')
# ele.send_keys('NBA')

# #定位百度首页-设置-将光标悬浮之上
# ele_Setting = driver.find_element(By.ID,'s-usersetting-top')
#
# sleep(3)

#引用ActionChains,进行一系列的鼠标模拟操作
# 1,鼠标右键--context_click
# ActionChains(driver).context_click(ele).perform()

# 2,鼠标双击操作-- double_click
# ActionChains(driver).double_click(ele).perform()

# # 3,鼠标悬浮操作-- double_click
# ActionChains(driver).move_to_element(ele_Setting).perform()

# 4,鼠标拖拽操作-- double_click
# ActionChains(driver).drag_and_drop_by_offset()


# #第一步,需定位滑块所在滑动条的所在位置
# slider = driver.find_element(By.CLASS_NAME,'txt')
# slider_Size = slider.size
# print(slider_Size)
#
# #第二步,需定位滑块的所在位置
# hk_Location = driver.find_element(By.CLASS_NAME,'btn')
#
#
# # #第三步,将滑块偏移到目标位置
# ActionChains(driver).drag_and_drop_by_offset().perform()



