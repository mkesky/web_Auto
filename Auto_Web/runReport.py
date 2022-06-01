from selenium import webdriver
import unittest
import time
from BeautifulReport import BeautifulReport


#加载测试文件
import Test_Case
from Test_Case import test_BaiDu
from Test_Case.test_BaiDu import Demo
# from Test_Case.test_BaiDu import BaiduTest



#discover方式加载测试用例
test_dir = "./"
discover = unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")


if __name__ == '__main__':

    # 按照一定格式获取当前时间
    now = time.strftime("%Y-%m-%d %H_%M_%S")

    # 定义报告存放路径
    fileLocation = './Report/' + now + '_result.html'



    #报告生成
    test_Report = BeautifulReport(discover)

    test_Report.report(
        filename = fileLocation,
        description = "测试报告",
        theme = "theme_default",
        report_dir = "."
    )








# with open(report_file, "wb") as fl:
#     module_path = "./"
#     # discover = unittest.defaultTestLoader.discover(start_dir=module_path, pattern="MyTestCase*.py")
#     # runner = HTMLTestRunner(title='测试标题', description='描述本次测试的大概内容', stream=fl)
#     # runner.run(discover)
#
#     discover = unittest.defaultTestLoader.discover(start_dir=module_path, pattern="MyTestCase*.py")
#     BeautifulReport(discover).report(description="tester", report_dir=report_dir, filename="can_report",
#                                      theme="theme_candy")
#     """
#     report_dir: 生成report的文件存储路径
#     filename: 生成文件的filename
#     description: 生成文件的注释
#     theme: 报告主题名
#     theme_default,theme_cyan,theme_candy,theme_memories
#     """



