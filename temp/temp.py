from selenium import webdriver
# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from common import read_yaml
import time
# import os
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import requests
requests.get(,)
class TestBaidu:
    def __init__(self):
        # options = webdriver.EdgeOptions()  # 创建Option类
        # browser_options = os.environ.get(
        #     "using_headless")  # 读取jekins配置的环境变量using_headless的值
        # print(f">>>>>>>> {browser_options}")
        # # print(f">>>>>>>> {os.environ}")
        # if browser_options and browser_options.lower() == "true":
        #     options.add_argument("--headless")
        self.driver = webdriver.Remote("http://192.168.106.129:5001/wd/hub",desired_capabilities=)
        self.driver.implicitly_wait(10)  # 隐式等待
        print("初始化driver")
        # yield driver
        # driver.quit()
        # print("关闭driver")

    def test1(self):
        self.driver.get("https://www.baidu.com")
        el1 = self.driver.find_element(By.CSS_SELECTOR,
                                       'input[class="bg s_btn"]')
        assert el1.get_attribute("value") == "百度一下"
        el2 = self.driver.find_element(By.CSS_SELECTOR, 'input[class="s_ipt"]')
        el2.send_keys("今日头条" + Keys.RETURN)
        time.sleep(3)
        assert "今日头条" in self.driver.title

    def test2(self):
        self.driver.get("https://www.baidu.com")
        el1 = self.driver.find_element(By.CSS_SELECTOR,
                                       'input[class="bg s_btn"]')
        assert el1.get_attribute("value") == "百度一下"
        el2 = self.driver.find_element(By.CSS_SELECTOR, 'input[class="s_ipt"]')
        el2.send_keys("今日" + Keys.RETURN)
        time.sleep(3)
        assert "今日" in self.driver.title

    def close(self):
        self.driver.quit()
        print("关闭driver")


if __name__ == "__main__":
    t = TestBaidu()
    t.test1()
    t.test2()
    time.sleep(3)
    t.close()
