"""
@Name: login_page.py
@Auth: 黄家健
@Date: 2022/11/27-18:46
"""
from PageLocators import login_locators as LL
from Common.base_page import BasePage


class LoginPage(BasePage):

    # 登录
    def login(self, username, password):
        caller_info = "登录页面_登录功能"
        self.click_element(LL.login_home_page, caller_info)
        self.input_text(LL.username_input, username, caller_info)
        self.input_text(LL.password_input, password, caller_info)
        self.click_element(LL.login_bnt, caller_info)

    # 注册
    def register(self):
        pass

    # 查询是否登录成功——能否找到退出按钮
    def logout_btn_isExist(self):
        return self.ele_isExist(LL.logout_bnt)

    # 退出登录
    def logout(self):
        if self.logout_btn_isExist():
            self.click_element(LL.logout_bnt)


