"""
@Name: login_locators.py
@Auth: 黄家健
@Date: 2022/12/18-13:30
"""
from selenium.webdriver.common.by import By


login_home_page = (By.XPATH, "//a[@href='user.php']")    # 登录首页
username_input = (By.XPATH, "//input[@name='username']")
password_input = (By.XPATH, "//input[@name='password']")
login_bnt = (By.XPATH, "//input[@name='submit']")

# 登录成功后的退出按钮
logout_bnt = (By.XPATH, "//a[text()='退出']")
