# webscraping-with-python
# use python to watch latest video of a Youtube Channel

from selenium import webdriver
url = "place link of channel's videos section of youtube"
browser = webdriver.Chrome()
browser.get(url)

browser.find_element_by_xpath('copy the xpath of recent video of the channel').click()
