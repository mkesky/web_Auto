from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep


# 打开Chrome浏览器
driver = webdriver.Chrome()

# 进入百度高级搜索页
url = "http://tieba.baidu.com/f/search/adv"
url_Trip = "https://www.ctrip.com/"
url_Multi = "C:\Testing\Attachment\Multi.html"
driver.get(url_Multi)
driver.maximize_window()

# 获取select下拉框的元素
# ele_Select = driver.find_element(By.NAME,'sm')
# sleep(3)

driver.f


# ele_Hotel = driver.find_element(By.XPATH,'//*[@id="kakxi"]/li[4]/div/div[1]/p')
sleep(3)


# 获取下拉框中所有选项元素（element）
# options_Select = Select(ele_Select).options
# print("所有选项元素的列表：%s" % options_Select)
#
#
# for i in options_Select:
#     print("元素对应的选项：%s" % i.text)


# 获取下拉框当前显示(选中)的元素(element)
# is_Selected = Select(ele_Select).all_selected_options
# print("被选中元素的列表：%s" % is_Selected)
#
#
# # 获取下拉框第一个被选中的元素
# first_Selected = Select(ele_Select).first_selected_option
# print("第一个被选中元素的列表：%s" % first_Selected)



# 通过select_by_index(self, index)选择下拉框元素
# Select(ele_Select).select_by_index(2)

# 通过select_by_value(self, value)选择下拉框元素
# Select(ele_Select).select_by_value("2")

# 通过select_by_visible_text(self, text)选择下拉框元素
# Select(ele_Select).select_by_visible_text('按相关性排序')

# 复选操作
Select(ele_Hotel).select_by_index(0)
sleep(3)
Select(ele_Hotel).select_by_index(1)

