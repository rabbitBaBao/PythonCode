"""
@Name: login_data.py
@Auth: 黄家健
@Date: 2022/12/15-20:29
"""

success_data = {"user": "admin123", "password": "admin123"}


# 异常用例
wrong_data = [
    {"user": "admin", "password": "admin123"},
    {"user": "admin", "password": "admin"},
    {"user": "admin", "password": "123"}
]

