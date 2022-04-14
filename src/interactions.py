from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Using Selenium - wait before completing an action
url = 'https://www.google.com/earth/'
driver = webdriver.Chrome()
driver.get(url)
wait = WebDriverWait(driver, 10)
launchEarthButton = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/header/div/nav[1]/ul[2]/li[2]/a/span/span')))
launchEarthButton.click()

#cd into the src directory then
#Run py interactions.py in the terminal (Windows)

"""
Why use Wait Functions?
- Many websites use asynchronous techniques to load content which causes a problem 
    when Selenium tries to locate an element that isn't loaded yet.
- Aides in avoiding exceptions or failing scripts due to an element not being available.

What do Wait Function do?
- They add crucial time intervals in between actions performed. Allowing the web driver 
    to wait until the element is loaded before it tries to interact with it. 

Two types of Wait Functions

Explicit Wait Functions
- Will wait until a condition is satisfied before executing.

Implicit Wait Functions
- Pulls the DOM for a certain amount of time, until the element becomes available.
"""