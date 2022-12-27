"""
@Name: test_login.py
@Auth: 黄家健
@Date: 2022/11/27-20:21
"""
import time
import TestData.login_data as LD
import pytest


@pytest.mark.usefixtures("access_web")
@pytest.mark.usefixtures("refresh_page")
class TestLogin:

    # 正常用例：登录成功
    @pytest.mark.smoke
    # fixture函数名称接受他的返回值
    def test_login_success(self, access_web):
        access_web[1].login(LD.success_data["user"], LD.success_data["password"])
        # 断言：能否找到退出按钮
        assert access_web[1].logout_btn_isExist()
        time.sleep(2)
        access_web[1].logout()

    # 用户名和密码为空
    def test_empty_input(self, access_web):
        access_web[1].login("", "")
        time.sleep(0.5)
        # 定位到到弹窗
        alert = access_web[0].switch_to.alert
        assert "用户名不能为空" in alert.text
        assert "登录密码不能为空" in alert.text
        time.sleep(1)
        alert.accept()
        time.sleep(1)

    @pytest.mark.parametrize("data", LD.wrong_data)
    # 用户名密码错误
    def test_login_wrong(self, data, access_web):
        access_web[1].login(data["user"], data["password"])
        # 断言：找不到退出按钮
        assert not access_web[1].logout_btn_isExist()
        time.sleep(1)

