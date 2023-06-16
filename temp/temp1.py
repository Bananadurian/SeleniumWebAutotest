#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

options = webdriver.EdgeOptions()
caps = {
    "browserName": "MicrosoftEdge",
    "browserVersion": "106.0",
    "platformName": "LINUX",
    "se:noVncPort": 7900,
    "se:vncEnabled": "true"
}
for key, value in caps.items():
    options.set_capability(key, value)
driver = webdriver.Remote(
    command_executor="http://192.168.106.129:4444/wd/hub", options=options)
driver.get("https://www.baidu.com")
el1 = driver.find_element(By.CSS_SELECTOR, 'input[class="bg s_btn"]')
assert el1.get_attribute("value") == "百度一下"
el2 = driver.find_element(By.CSS_SELECTOR, 'input[class="s_ipt"]')
el2.send_keys("今日头条" + Keys.RETURN)
time.sleep(10)
assert "今日头条" in driver.title
driver.quit()