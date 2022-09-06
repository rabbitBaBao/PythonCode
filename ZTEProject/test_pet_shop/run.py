"""
@Name: run.py
@Auth: 黄家健
@Date: 2022/8/29-21:33
"""
import unittest
from test_case import TestPetShop
import HTMLTestRunner

suit = unittest.TestSuite()

# 加载所有用例
loader = unittest.TestLoader()
suit.addTest(loader.loadTestsFromTestCase(TestPetShop))

# 测试执行简单用法
# runner = unittest.TextTestRunner()
# runner.run(suit)

# 测试执行并生成测试报告
# with open('test_report.txt', 'w+', encoding='utf-8') as file:         # 使用with可以防止忘记关闭文件
#     runner = unittest.TextTestRunner(stream=file, verbosity=2)   # verbosity = 0/1/2，设置测试报告的详细程度
#     runner.run(suit)
# print(file.closed)  # 判断是否关闭，返回ture说明已经关了

# 使用外部库HTMLTestRunner生成更加漂亮的测试报告
with open('test_report.html', 'wb') as file:         # 使用with可以防止忘记关闭文件
    runner = HTMLTestRunner.HTMLTestRunner(stream=file, verbosity=2, title='宠物店测试报告')
    runner.run(suit)
