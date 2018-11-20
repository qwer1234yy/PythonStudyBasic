from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver = webdriver.Firefox()
driver.get("http://www.ctrip.com")
# 进入首页
indexPage = driver.find_element_by_id("c_ph_hp")
indexPage.click()
# scan the elements
hotel_international = driver.find_element_by_xpath("//p[@id='hotelSwitch']/a[text()='海外酒店']")
hotel_international.click()
time.sleep(1)
hotel_team = driver.find_element_by_xpath("//p[@id='hotelSwitch']/a[text()='酒店团购']")
hotel_team.click()
time.sleep(1)
hotel_views = driver.find_element_by_xpath("//p[@id='hotelSwitch']/a[text()='酒店+景点']")
hotel_views.click()
time.sleep(1)
hotel_meeting = driver.find_element_by_xpath("//p[@id='hotelSwitch']/a[text()='会议•团房•长住']")
hotel_meeting.click()
time.sleep(1)
hotel_domestic = driver.find_element_by_xpath("//p[@id='hotelSwitch']/a[text()='国内酒店']")
hotel_domestic.click()
time.sleep(1)

# book domestic hotel
# hotel name in domestic
hotel_city = driver.find_element_by_id("HD_CityName")
# hotel_city.send_keys("北京")
hotel_city.click()
# select city
select_city = driver.find_element_by_link_text("上海")
select_city.click()

# Drag and drop
ctripLogo = driver.find_element_by_xpath("//a[@title='携程旅行网']")
searchBox = driver.find_element_by_id("_allSearchKeyword")
action_chains = ActionChains(driver)
action_chains.drag_and_drop(ctripLogo, searchBox).perform()
# select_city.__getitem__(0).click()
# 酒店页面
# holtel_page = driver.find_element_by_class_name("cui_nav_has")
# holtel_page.click()