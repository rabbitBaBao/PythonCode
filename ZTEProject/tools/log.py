"""
@Name: log.py
@Auth: ZTE黄家健
@Date: 2022/8/30-23:05
@Email:huang.jiajian@zte.com.cn
"""
import logging
import os
import time
"""
Logger 即记录器，Logger提供了日志相关功能的调用接口。
Handler 即处理器，将（记录器产生的）日志记录发送至合适的目的地。
Filter 即过滤器，提供了更好的粒度控制，它可以决定输出哪些日志记录。
Formatter 即格式化器，指明了最终输出中日志记录的格式。
"""


class Logging:
    @staticmethod
    def make_log_dir(dirname='logs'):  # 创建存放日志的目录，并返回目录的路径
        now_dir = os.path.dirname(__file__)
        father_path = os.path.split(now_dir)[0]
        path = os.path.join(father_path, dirname)
        path = os.path.normpath(path)
        if not os.path.exists(path):
            os.mkdir(path)
        return path

    def get_log_filename(self):  # 创建日志文件的文件名格式，便于区分每天的日志
        filename = "{}.log".format(time.strftime("%Y-%m-%d", time.localtime()))
        filename = os.path.join(self.make_log_dir(), filename)
        filename = os.path.normpath(filename)
        return filename

    def log(self, level='DEBUG'):  # 生成日志的主方法,传入对那些级别及以上的日志进行处理
        logger = logging.getLogger()  # 创建日志器
        # print(getattr(logging, level))
        level = level.upper()  # 传入参数全部变成大写
        level = getattr(logging, level)  # 获取日志模块的的级别对象属性值，level从字符串变成数字
        # print(level)
        logger.setLevel(level)  # 设置日志级别，此时level是一个数字
        if not logger.handlers:  # 作用,防止重新生成处理器
            sh = logging.StreamHandler()  # 创建控制台日志处理器
            fh = logging.FileHandler(filename=self.get_log_filename(), mode='a', encoding="utf-8")  # 创建日志文件处理器
            # 创建格式器
            fmt = logging.Formatter("%(asctime)s-%(levelname)s-%(filename)s-Line:%(lineno)d-Message:%(message)s")
            # 给处理器添加格式
            sh.setFormatter(fmt=fmt)
            fh.setFormatter(fmt=fmt)
            # 给日志器添加处理器，过滤器一般在工作中用的比较少，如果需要精确过滤，可以使用过滤器
            logger.addHandler(sh)
            logger.addHandler(fh)
        return logger  # 返回日志器


# 生成对象实例，供其他文件使用
run_log = Logging().log(level='info')
# run_log.debug("1111111111111111111111")  # 使用日志器生成日志
# run_log.info("222222222222222222222222")
# run_log.error("111")
# run_log.warning("3333333333333333333333333333")
# run_log.critical("44444444444444444444444444")

