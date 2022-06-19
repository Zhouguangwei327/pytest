import os
from utils.times import strf_times


class ConfigManager(object):

    def __init__(self):
        # 项目绝对路径
        self.BASE_PATH = os.path.dirname(os.path.dirname(os.path.join(__file__)))

    @property
    def log_file(self):
        """
        :return: 日志文件绝对路径
        """
        log_dir = os.path.join(self.BASE_PATH, 'log')
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
        return os.path.join(self.BASE_PATH, 'log', '%s.log' % strf_times())

    @property
    def config_file(self):
        """
        :return: 配置文件的绝对路径
        """
        config_file = os.path.join(self.BASE_PATH, 'config', 'config.ini')
        if not os.path.exists(config_file):
            raise FileNotFoundError('%s no such file or directory' % config_file)
        return config_file

    @property
    def data_file(self):
        """
        :return: 测试数据的绝对路径
        """
        date_file = os.path.join(self.BASE_PATH, 'data', 'data.xls')
        if not os.path.exists(date_file):
            raise FileNotFoundError('%s no such file or directory' % date_file)
        return date_file


cm = ConfigManager()
if __name__ == '__main__':
    # print(cm.BASE_PATH)
    # print(cm.log_file)
    print(cm.config_file)
    print(cm.data_file)
