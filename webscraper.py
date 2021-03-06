from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.youtube.com/c/DisguisedToast/videos')

driver.find_element_by_xpath('//*[@id="thumbnail"]').click()