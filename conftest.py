from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from common import read_yaml
import pytest
import os


@pytest.fixture(scope="session", autouse=True)
def init_webdriver():
    options = webdriver.EdgeOptions()  # 创建Option类
    browser_options = os.environ.get(
        "using_headless")  # 读取jekins配置的环境变量using_headless的值
    print(f">>>>>>>> {browser_options}")
    # print(f">>>>>>>> {os.environ}")
    if browser_options and browser_options.lower() == "true":
        options.add_argument("--headless")
    driver = webdriver.Edge(service=EdgeService(
        EdgeChromiumDriverManager().install()),
                            options=options)
    driver.implicitly_wait(10)  # 隐式等待
    print("初始化driver")
    yield driver
    driver.quit()
    print("关闭driver")
