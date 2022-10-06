from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class TestBaidu:
    def test1(self, init_webdriver):
        driver = init_webdriver
        driver.get("https://www.baidu.com")
        el1 = driver.find_element(By.CSS_SELECTOR, 'input[class="bg s_btn"]')
        assert el1.get_attribute("value") == "百度一下"
        el2 = driver.find_element(By.CSS_SELECTOR, 'input[class="s_ipt"]')
        el2.send_keys("今日头条" + Keys.RETURN)
        time.sleep(3)
        assert "今日头条" in driver.title

    def test2(self, init_webdriver):
        driver = init_webdriver
        driver.get("https://www.baidu.com")
        el1 = driver.find_element(By.CSS_SELECTOR, 'input[class="bg s_btn"]')
        assert el1.get_attribute("value") == "百度一下"
        el2 = driver.find_element(By.CSS_SELECTOR, 'input[class="s_ipt"]')
        el2.send_keys("今日" + Keys.RETURN)
        time.sleep(3)
        assert "今日" in driver.title