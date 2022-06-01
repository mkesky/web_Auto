from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from time import sleep

# driver = webdriver.Chrome()
#
# #访问地址
# url = "https://www.baidu.com/"
# youdao = "https://www.youdao.com/"
# url002 = "https://www.autohome.com.cn/nanjing/"
# # url = "https://mail.126.com/"
# driver.get(url)
# driver.maximize_window()
# sleep(5)
# # driver.set_window_size(800,700)
# driver.implicitly_wait(10)
#通过ID定位元素
# ele = driver.find_element(By.ID,'kw')
# News = driver.find_element(By.LINK_TEXT,'新闻')
# Button = driver.find_element(By.ID,'su')
# sele = driver.find_element(By.CSS_SELECTOR,"[type='checkbox']")
# print(ele.size)
# print(News.text)
# print(News.is_displayed())
# print(Button.is_enabled())
# print(sele.is_selected())


# 获取标签之间的文本内容
# print(News.get_attribute('href'))
#
# # 获取元素内的全部HTML
# print(News.get_attribute('target'))
# print(News.get_attribute('class'))
# # # 获取标签之间的文本内容
# print(News.get_attribute('textContent'))
#
# # 获取元素内的全部HTML
# print(News.get_attribute('innerHTML'))
# # # 获取包含选中元素的HTML
# # print(News.get_attribute('outerHTML'))
# driver.quit()
#通过NAME定位元素
# driver.find_element(By.NAME,'wd').send_keys("NBA")

#通过CLASS_NAME定位元素
# driver.find_element(By.CLASS_NAME,'s_ipt').send_keys('512')

#通过TAG_NAME定位元素
# driver.find_element(By.TAG_NAME,'value').send_keys('512')

#通过LINK_TEXT定位元素
# driver.find_element(By.LINK_TEXT,'新闻').click()

#通过PARTIAL_LINK_TEXT定位元素
# driver.find_element(By.PARTIAL_LINK_TEXT,'新').click()

#通过XPATH定位元素
# driver.find_element(By.XPATH,"//*[@id='kw']").send_keys("NBA")


#通过CSS_SELECTOR定位元素
# driver.find_element(By.CSS_SELECTOR,'#kw').send_keys("端午")
# driver.find_element(By.CSS_SELECTOR,'.s_ipt').clear()
# driver.find_element(By.CSS_SELECTOR,'.s_ipt').send_keys("端午")
# sleep(3)
# driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
# driver.quit()
# time.sleep(3)

# driver.refresh()
# driver.back(youdao)
# time.sleep(3)
# driver.forward(youdao)

# driver.find_element(By.ID,'kw').send_keys("NBA")
# driver.find_element(By.CSS_SELECTOR,"[type='submit']").submit()


#浏览器页面信息获取
# url_Today = driver.current_url  #当前页面url
# current_Title = driver.title   #当前页面标题
# current_Name = driver.name     #当前浏览器名称
# current_Page_Source = driver.page_source
#
#
# #打印所需浏览器信息
# print(url_Today)
# print(current_Title)
# print(current_Name)
# print(current_Page_Source)



# print("one")
#
# if __name__=="__main__":
#     print("two")




class Demo(unittest.TestCase):
    def setUp(self):
        print("测试开始")


    def test_001(self):
        print("这里是第一条测试用例")

    def test_002(self):
        print("这里是第二条测试用例")

    def rain(self):
        print("这里是第三条测试用例")


    def tearDown(self):
        print("测试结束")


if __name__ == '__main__':
    unittest.main()