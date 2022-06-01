from selenium import webdriver
import unittest
import time


#加载测试文件
import Test_Case
from Test_Case import test_BaiDu
from Test_Case.test_BaiDu import Demo
# from Test_Case.baidu import Demo

# from Test_Case.test_BaiDu import BaiduTest



#测试过套件test suite方式加载测试用例
# 构造测试集
suite = unittest.TestSuite()
# suite.addTest(BaiduTest("test_baidu"))

suite.addTest(Demo("test_003"))
suite.addTest(Demo("test_002"))
# suite.addTest(Demo("rain"))



if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite)  #运行测试用例


