"""
@Name: project_path.py
@Auth: 黄家健
@Date: 2022/8/29-20:58
"""
import os
'''专门读取文件路径'''
now_dir = os.path.dirname(__file__)
project_path = os.path.split(now_dir)[0]

tset_case_path = os.path.join(project_path, 'test_data', 'test_case.xlsx')
config_path = os.path.join(project_path, 'config', 'case.ini')

