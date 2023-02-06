import time

from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = ChromeOptions()
options.add_experimental_option('detach', True)

web = Chrome(options=options)



web.get("http://lagou.com")

el = web.find_element(By.XPATH, '//*[@id="changeCityBox"]/p[1]/a')
el.click()

time.sleep(1)

web.find_element(By.XPATH, '//*[@id="search_input"]').send_keys("python", Keys.ENTER)

li_list = web.find_elements(By.XPATH, '//*[@id="jobList"]/div[1]/div')

time.sleep(2)

for li in li_list:
    job_name = li.find_element(By.XPATH, './div[1]/div[1]/div[1]/a').text
    job_price = li.find_element(By.XPATH, './div[1]/div[1]/div[2]/span').text
    company_name = li.find_element(By.XPATH, './div[1]/div[2]/div[1]/a').text
    print(job_name, job_price, company_name)

web.find_element(By.XPATH, '//*[@id="jobList"]/div[1]/div[1]').click()
web.switch_to.window(web.window_handles[-1])

job_detail = web.find_element(By.XPATH, '//*[@id="job_detail"]/dd[2]/div').text
print(job_detail)

web.close()

web.switch_to.window(web.window_handles[0])
print(web.find_element(By.XPATH, '//*[@id="jobList"]/div[1]/div[1]').text)

