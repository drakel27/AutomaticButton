import time
# importing webdriver from selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# Here Edge  will be used
driver = webdriver.Chrome(ChromeDriverManager().install())
 
# URL of website
url = "https://github.com/drakel27/AutomaticButton/blob/main/index.html"
 
# Opening the website
driver.get(url)
 
# getting the button by class name
button = driver.find_element_by_id("button")

# wait to click the button
time.sleep(7)
 
# clicking on the button
button.click()

exit()
