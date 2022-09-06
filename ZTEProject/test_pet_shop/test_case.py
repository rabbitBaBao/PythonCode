"""
@Name: test_case.py
@Auth: ZTE黄家健
@Date: 2022/8/26-22:07
@Email:huang.jiajian@zte.com.cn
"""
import unittest
import requests
from tools.doexecl import DoExcel
from tools.project_path import tset_case_path, config_path
from tools.log import run_log as log
from ddt import ddt, data, unpack, file_data
from config.read_config import ReadConfig
import re

# 请先在配置文件配置需要执行的用例
mode = ReadConfig.read_config(config_path, 'Mode', 'queryPetInfo')
cases_list = DoExcel(tset_case_path, 'queryPetInfo').get_excel_test_case(mode)

mode = ReadConfig.read_config(config_path, 'Mode', 'createPet')
cases_list2 = DoExcel(tset_case_path, 'createPet').get_excel_test_case(mode)

post_data = DoExcel(tset_case_path, 'stringReplace').get_excel_test_case()
data_replace = {}   # post_data是一个字典列表，只有一个元素。
for data_item in post_data:
    data_replace = data_item  # 取出字符串替换字典


@ddt  # 声明了ddt类装饰器
class TestPetShop(unittest.TestCase):

    def setUp(self):   # 重写父类方法，setUp在用例执行之前会执行一次，源码啥也没做只有一个pass
        log.info("用例开始执行")

    def tearDown(self):  # 重写父类方法,tearDown在用例执行之后会执行一次，源码啥也没做只有一个pass
        log.info("用例执行结束")

    @data(*cases_list)  # @dta(*testadata)：*号意为解包，ddt会按逗号分隔，将数据拆分（不需要@unpack方法装饰器了）
    def test_queryPetInfo(self, test_case):
        url = test_case['UrlFormat'].replace('${petId}', str(test_case['Url_petId']))
        # url = "1111"
        try:
            res = requests.request(test_case['Method'], url)
            self.assertEqual(test_case['status_code'], res.status_code)
        except Exception as error:
            log.error('用例{0}:{1}执行失败:{2}'.format(test_case['CaseId'],  test_case['Title'], error))
            raise error
        else:
            log.info('用例{0}:{1} 测试通过'.format(test_case['CaseId'], test_case['Title']))

    @data(*cases_list2)  # @dta(*testadata)：*号意为解包，ddt会按逗号分隔，将数据拆分（不需要@unpack方法装饰器了）
    def test_createPet(self, test_case):
        test_case_data = eval(test_case['Data'])
        print(test_case_data)
        print(type(test_case_data))
        for key in test_case_data.keys():
            # 在${name1}中找出name1
            res = re.search('\$\{(.*?)\}', test_case_data[key])
            # test_case_data['name'] = data_replace['name1']
            test_case_data[key] = data_replace[res.group(1)]
        print(test_case_data)
        try:
            res = requests.request(test_case['Method'], test_case['UrlFormat'], data=test_case_data)
            self.assertEqual(test_case['status_code'], res.status_code)
        except Exception as error:
            log.error('用例{0}:{1}执行失败:{2}'.format(test_case['CaseId'],  test_case['Title'], error))
            raise error
        else:
            log.info('用例{0}:{1} 测试通过'.format(test_case['CaseId'], test_case['Title']))


if __name__ == '__main__':
    unittest.main()


