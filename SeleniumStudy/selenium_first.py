from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time


driver = webdriver.Firefox()
driver.get("http://www.python.org")
time.sleep(3)
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
# driver.page_source()
driver.close()
# Filling in forms
element = driver.find_element_by_xpath("//select[@name='name']")
all_options = element.find_elements_by_tag_name("option")
for option in all_options:
    print("Value is: %s" % option.get_attribute("value"))
    option.click()
# this isn’t the most efficient way of dealing with SELECT elements. WebDriver’s
# support classes include one called a “Select”
select = Select(driver.find_element_by_name('name'))
select.select_by_index(0)
select.select_by_visible_text("text")
select.select_by_value("value")
select.deselect_all()