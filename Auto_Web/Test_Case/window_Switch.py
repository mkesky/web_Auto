from selenium import webdriver
from selenium.webdriver.common.by import By
import time



# driver = webdriver.Chrome()
#
# #访问地址
# url = "https://www.baidu.com/"
# driver.get(url)
# driver.maximize_window()
# driver.implicitly_wait(10)

# #产生第二个页面
# driver.find_element(By.LINK_TEXT,'新闻').click()
#
# #获得所有窗口的句柄Handle
# all = driver.window_handles
# print("所有页签handle %s" % all)
#
# #打印当前窗口的句柄current_Handle
# current_Handle = driver.current_window_handle
# print("当前页面handle %s" % current_Handle)
#
# #此时,title01打印的是百度首页,因为页签还未切换过来
# title01 = driver.title
# print("切换前title %s" % title01)
# time.sleep(3)
#
# #进行页签之间的切换
# driver.switch_to.window(all[1])
#
# #此时,页签也切换至百度新闻页,打印的是百度新闻的title
# current_Title = driver.title
# print(current_Title)




import test_BaiDu

def he():
    print('一会吃什么')
if __name__=="__main__":
    test_BaiDu.chi()
    he()
print("test2的__name__:"+__name__)





