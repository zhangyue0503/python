from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = ChromeOptions()
options.add_experimental_option('detach', True)

web = Chrome(options=options)

web.get("https://kyfw.12306.cn/otn/resources/login.html")

