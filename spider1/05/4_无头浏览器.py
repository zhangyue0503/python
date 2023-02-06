import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disable-gpu")

web = Chrome(options=opt)

web.get("https://www.endata.com.cn/BoxOffice/BO/Year/index.html")

time.sleep(2)
# sel_el = web.find_element(By.XPATH, '//*[@id="OptionDate"]')
# sel = Select(sel_el)
#
# for i in range(len(sel.options)):
#     sel.select_by_index(i)
#     time.sleep(2)
#     table = web.find_element(By.XPATH, '//*[@id="TableList"]/table')
#     print(table.text)

print(web.page_source)

web.close()

