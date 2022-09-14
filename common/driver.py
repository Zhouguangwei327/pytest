from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class Driver:
    def __init__(self):
        self.driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    # 打开浏览器
    def open_browser(self, url='https://www.baidu.com'):
        self.driver.get(url)
        return self.driver

    # 窗口最大化
    def max_window(self):
        return self.driver.maximize_window()

    # 窗口最小化
    def min_window(self):
        return self.driver.minimize_window()

    # 关闭窗口
    def close_browser(self):
        return self.driver.quit()


driver = Driver()
if __name__ == '__main__':
    driver.open_browser()
    driver.close_browser()
