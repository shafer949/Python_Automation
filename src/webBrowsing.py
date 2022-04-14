from selenium import webdriver

#Use Selenium to interact with a form
url = 'http://demo.seleniumeasy.com/basic-first-form-demo.html'
driver = webdriver.Chrome()
driver.get(url)

#Right click on field > Inspect > Right click html element > Copy > Copy XPath
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys("Hello World")
showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click()
additionField1 = driver.find_element_by_xpath('//*[@id="sum1"]')
additionField1.send_keys('10')
additionField2 = driver.find_element_by_xpath('//*[@id="sum2"]')
additionField2.send_keys('12')
getTotalButton = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
getTotalButton.click()

#Run py webBrowsing.py in the terminal (Windows)