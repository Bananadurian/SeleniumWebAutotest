from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from common import read_yaml
import pytest


@pytest.fixture(scope="session", autouse=True)
def init_webdriver():
    options = webdriver.EdgeOptions()  # 创建Option类
    browser_options = read_yaml.get_config("BrowserOptions")
    if browser_options and browser_options.get("args"):
        args_list = browser_options.get("args")
        for arg in args_list:
            options.add_argument(arg)
    driver = webdriver.Edge(service=EdgeService(
        EdgeChromiumDriverManager().install()),
                            options=options)
    driver.implicitly_wait(10)  # 隐式等待
    print("初始化driver")
    yield driver
    driver.quit()
    print("关闭driver")
