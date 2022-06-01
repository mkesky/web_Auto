from selenium import webdriver
import unittest
import time


#加载测试文件
import Test_Case
from Test_Case import test_BaiDu
# from Test_Case.test_BaiDu import BaiduTest

from Test_Case.test_BaiDu import Demo


#discover方式加载测试用例
test_dir = "./Test_Case/"


#TestLoader类中提供的discover（）⽅法可以⾃动识别测试⽤例
discover = unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")


if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(discover)

