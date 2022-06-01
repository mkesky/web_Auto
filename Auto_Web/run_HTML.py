from selenium import webdriver
import unittest
import time
from HTMLTestRunner import HTMLTestRunner
# from common.BeautifulReport import BeautifulReport

#加载测试文件
import Test_Case
from Test_Case import test_BaiDu
from Test_Case.test_BaiDu import Demo
# from Test_Case.baidu import Demo

# from Test_Case.test_BaiDu import BaiduTest


#测试过套件test suite方式加载测试用例
# 构造测试集
suite = unittest.TestSuite()
suite.addTest(Demo("test_003"))
suite.addTest(Demo("test_002"))

if __name__ == '__main__':

    # 按照一定格式获取当前时间
    now = time.strftime("%Y-%m-%d %H_%M_%S")

    # 定义报告存放路径
    fileLocation = './Report/' + now + '_result.html'
    fp = open(fileLocation, 'wb')

    # 定义测试报告
    runner = HTMLTestRunner(
        stream=fp,
        title='百度和有道搜素测试报告',
        description='用例执行情况'
    )

    runner.run(suite)  #运行测试用例
    fp.close()         #关闭报告文件
