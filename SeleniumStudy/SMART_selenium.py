from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get('http://strzw058051/SMARTSolutions/')

login_ele = driver.find_element_by_id('txtLoginid')
password_ele = driver.find_element_by_id('txtPassword')
login_ele_btn = driver.find_element_by_id('btnloginText')

login_ele.clear()
login_ele.send_keys('admin')
password_ele.clear()
password_ele.send_keys('Admin')
login_ele_btn.click()

try:
    element = WebDriverWait(driver, 600).until(
        EC.presence_of_element_located((By.ID, "spUserName"))
    )
    print('wait')
finally:
    print(driver.current_url)
