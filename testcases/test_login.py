from common.driver import driver
import pytest


class TestLogin:

    def setup(self, method):
        pass

    def test_login(self):
        driver.open_browser()
        driver.driver.set_window_size(1920, 1080)

    def teardown(self):
        driver.close_browser()


if __name__ == '__main__':
    pytest.main(['-s', '/testcases/test_login.py'])
