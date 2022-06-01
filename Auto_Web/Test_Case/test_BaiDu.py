from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from time import sleep


class Demo(unittest.TestCase):
    def setUp(self):
        print("测试开始")

    def test_003(self):
        print("这里是第一条测试用例")

    def test_002(self):
        print("这里是第二条测试用例")

    def rain(self):
        print("这里是第三条测试用例")


    def tearDown(self):
        print("测试结束")


if __name__ == '__main__':
    unittest.main()




# class Demo_002(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         print("测试开始")
#
#
#     def test_001(self):
#         print("这里是第一条测试用例")
#
#     def test_002(self):
#         print("这里是第二条测试用例")
#
#
#     @classmethod
#     def tearDownClass(cls):
#         print("测试结束")
#
# if __name__ == '__main__':
#     unittest.main()






# class Test(unittest.TestCase):
#
#     def setUp(self):
#         pass
#
#     @unittest.skip("暂不执行该用例")
#     def test_1(self):
#         print(1111)
#
#     # 第一个条件返回值为true时 跳过执行 ，第二个参数为说明原因
#     @unittest.skipIf(1==2, "1=1,条件为真,返回值为True,跳过该用例")
#     def test_2(self):
#         print(222)
#
#     # 第一个条件返回值为true时执行 第二个参数为说明原因
#     @unittest.skipUnless(1==1, "1等于1 返回值为True执行")
#     def test_3(self):
#         print(3333)
#
#     # 标记该测试预期为失败 ，如果该测试方法运行失败，则该测试不算做失败
#     @unittest.expectedFailure
#     def test_4(self):
#         print(444)
#
#
#     def tearDown(self):
#         pass
#
#
# if __name__ == "__main__":
#     unittest.main()







# def chi():
#     print('晚饭吃什么')

# if __name__=="__main__":
#     chi()
#
# print("test1的__name__:"+__name__)




# class Test(unittest.TestCase):
#
#     def setUp(self):
#         pass
#
#     @unittest.skip("无条件跳过")
#     def test_1(self):
#         print(1111)
#
#     # 第一个条件返回值为true时 跳过执行 ，第二个参数为说明原因
#     @unittest.skipIf(1==1, "1等于1 返回值为True跳过执行")
#     def test_2(self):
#         print(222)
#
#     # 第一个条件返回值为true时执行 第二个参数为说明原因
#     @unittest.skipUnless(1==1, "1等于1 返回值为True执行")
#     def test_3(self):
#         print(3333)
#
#     #标记该测试预期为失败 ，如果该测试方法运行失败，则该测试不算做失败
#     @unittest.expectedFailure
#     def test_4(self):
#         print(111)
#
#
#     def tearDown(self):
#         pass
#
#
# if __name__ == "__main__":
#     unittest.main()




# class BaiduTest(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(10)
#         self.driver.maximize_window()
#         self.url = "https://www.baidu.com/"
#
#     def test_baidu(self):
#         driver = self.driver
#         driver.get(self.url)
#         driver.find_element(By.ID,'kw').clear()
#         driver.find_element(By.ID, 'kw').send_keys("NBA")
#         driver.find_element(By.ID, 'su').submit()
#         sleep(5)
#         title = driver.title
#         #2种断言方式随便用哪种
#         # self.assertEqual(title,u"fbsdbsfbsdfsfbdfsbfdsbfdsbd")
#         # self.assertTrue(1==2,"Who are you ?")
#         # self.assertIs("百度安全验证",title)
#         self.assertIn(title,"NBA")
#
#
#         assert title == "NBA_百度搜索"
#         print(title)
#
#     def tearDown(self):
#         self.driver.quit()
#
#
# if __name__ == "__main__":
#     unittest.main()



from Test_Case import baidu

# def snow():
#     print('下雪了')
#
# if __name__=="__main__":
#     snow()

    # baidu.rain()

