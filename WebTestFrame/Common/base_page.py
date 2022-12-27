"""
@Name: base_page.py
@Auth: 黄家健
@Date: 2022/12/18-13:07
"""
# 封装基本函数、执行日志、失败截图、异常处理
from Common.log import run_log as log
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # 等待元素可见
    def wait_eleVisible(self, locator, times=10, poll_frequency=0.5, caller_info=""):
        """
        :param locator: 元素定位信息
        :param times:
        :param poll_frequency:
        :param caller_info: 调用时的模块名_页面名_操作名称
        :return:
        """
        log.info("等待元素{0}可见".format(locator))
        try:
            WebDriverWait(self.driver, times, poll_frequency).until(EC.visibility_of_element_located(locator))
        except:
            log.exception("等待元素可见失败")
            # 截图
            self.save_screenshot(caller_info)
            raise

    # 等待元素存在
    def wait_elePresence(self):
        pass

    # 判断元素是否存在
    def ele_isExist(self, locator):
        log.info("判断元素{0}是否存在".format(locator))
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    # 查找元素
    def get_element(self, locator, caller_info=""):
        log.info("查找元素{0}".format(locator))
        try:
            return self.driver.find_element(*locator)
        except:
            log.exception("查找元素失败")
            self.save_screenshot(caller_info)
            raise

    # 点击操作
    def click_element(self, locator, caller_info=""):
        ele = self.get_element(locator, caller_info)
        log.info("点击元素{0}".format(locator))
        try:
            ele.click()
        except:
            log.exception("点击元素失败")
            self.save_screenshot(caller_info)
            raise

    # 输入操作
    def input_text(self, locator, text, caller_info=""):
        ele = self.get_element(locator, caller_info)
        try:
            ele.send_keys(text)
        except:
            log.exception("输入失败")
            self.save_screenshot(caller_info)
            raise

    # 获取文本
    def get_text(self, locator, caller_info=""):
        ele = self.get_element(locator, caller_info)
        try:
            return ele.text
        except:
            log.exception("获取文本失败")
            self.save_screenshot(caller_info)
            raise

    # 获取元素属性
    def get_eleAttribute(self, locator, attr, caller_info=""):
        ele = self.get_element(locator, caller_info)
        try:
            return ele.get_attribute(attr)
        except:
            log.exception("获取树形失败")
            self.save_screenshot(caller_info)
            raise

    # alert处理
    def alert_action(self, action="accept"):
        pass

    # iframe切换
    def switch_iframe(self, iframe_reference):
        pass

    # 上传操作
    def upload_file(self):
        pass

    # 截图操作
    def save_screenshot(self, file_name_header):
        # 创建文件夹保存图片
        now_dir = os.path.dirname(__file__)
        father_path = os.path.split(now_dir)[0]
        path = os.path.join(father_path, "Screenshot")
        path = os.path.normpath(path)
        if not os.path.exists(path):
            os.mkdir(path)

        # 图片文件名称：模块名_页面名_操作名称_时间
        file_name = file_name_header + "{}.png".format(time.strftime("%Y-%m-%d", time.localtime()))
        picture_file = os.path.join(path, file_name)
        picture_file = os.path.normpath(picture_file)
        self.driver.save_screenshot(picture_file)

