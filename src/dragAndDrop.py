from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

#Using Selenium to complete a drag and drop interaction
url = 'http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
source = driver.find_element_by_xpath('//*[@id="box3"]')
destination = driver.find_element_by_xpath('//*[@id="box103"]')
actions = ActionChains(driver)
actions.drag_and_drop(source, destination).perform()

#cd into the src directory then
#Run py dragAndDrop.py in the terminal (Windows)
