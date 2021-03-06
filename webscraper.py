from selenium import webdriver

driver = webdriver.Chrome()
driver.get('paste the link of videos section of the channel')

driver.find_element_by_xpath('paste the xpath of latest video of the channel by inspecting').click()
