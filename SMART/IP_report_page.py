from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


def go_to_report(self, driver, report_name):

    Case_Listing_link = driver.find_element_by_link_text(report_name)
    ActionChains(driver).double_click(Case_Listing_link).perform()