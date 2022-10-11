from appium import webdriver
import time

desired_caps = {
    "platformName": "Android",
    "platformVersion": "8.1",
    "deviceName": "aa",
    "udid": "192.168.235.102:5555",
    "noReset": "false",
    "appPackage": "com.android.settings",
    "appActivity": "com.android.settings.Settings"
}
appium_server_url = "http://localhost:4723/wd/hub"
driver = webdriver.Remote(appium_server_url, desired_caps)

time.sleep(5)
driver.quit()
