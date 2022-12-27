"""
@Name: conftest.py
@Auth: 黄家健
@Date: 2022/12/24-18:26
"""
import pytest
from selenium import webdriver
from PageObject.login_page import LoginPage
from TestData import common_data as CD


driver = None


@pytest.fixture(scope="class")
def access_web():
    global driver
    # 前置操作
    driver = webdriver.Chrome()
    driver.get(CD.login_url)
    lg = LoginPage(driver)
    yield driver, lg   # 返回值
    # 后置操作
    driver.quit()


@pytest.fixture(scope="function")
def refresh_page():
    global driver
    # 前置操作
    yield
    # 后置操作
    driver.refresh()

