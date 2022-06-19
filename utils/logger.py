import logging
from config.conf import cm


class Logger(object):
    def __init__(self):
        self.logger = logging.getLogger()
        if logging.FileHandler(cm.log_file):
            self.logger.setLevel(logging.DEBUG)

            fh = logging.FileHandler(cm.log_file, encoding='utf-8')
            sh = logging.StreamHandler()

            fh.setLevel(logging.DEBUG)
            sh.setLevel(logging.DEBUG)

            fmt = logging.Formatter('[%(asctime)s][%(levelname)s][%(filename)s.%(lineno)d]\t%(message)s')

            fh.setFormatter(fmt)
            sh.setFormatter(fmt)

            self.logger.addHandler(fh)
            self.logger.addHandler(sh)


log = Logger().logger
if __name__ == '__main__':
    log.info('hello')
