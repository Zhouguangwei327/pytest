import datetime


def strf_times(fmt='%Y%m%d'):
    """
    :param fmt: 时间格式
    :return: 返回时间戳
    """
    return datetime.datetime.utcnow().strftime(fmt)


if __name__ == '__main__':
    print(strf_times())
