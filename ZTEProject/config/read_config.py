"""
@Name: read_config.py
@Auth: ZTE黄家健
@Date: 2022/9/3-9:58
@Email:huang.jiajian@zte.com.cn
"""
import configparser


class ReadConfig:
    @staticmethod
    def read_config(file_name, section, option):
        cf = configparser.ConfigParser()
        cf.read(file_name, encoding='utf-8')
        return cf.get(section, option)


if __name__ == '__main__':
    res = ReadConfig.read_config('case.ini', 'Mode', 'queryPetInfo')
    print(res)
    print(type(res))
    res = ReadConfig.read_config('case.ini', 'User', 'password')
    print(res)
    if res == '123456':
        print(1)
    else:
        print(2)
