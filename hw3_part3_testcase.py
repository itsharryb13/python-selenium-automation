from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome(executable_path='/Users/bavaharpreetbhalla/internship/python-selenium-automation/chromedriver')
driver.maximize_window()

driver.get('https://www.amazon.com/gp/help/customer/display.html')

search = driver.find_element(By.ID,'helpsearch')
search.clear()
search.send_keys('Cancel Order')



search.send_keys(Keys.RETURN)

#verify
expected_result = 'Cancel Order'
actual_result= driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div/div[1]/div/div/form/div/p/b").text

assert expected_result == actual_result, f"expected text {expected_result} is same as {actual_result}"
print('Test Passed')
driver.quit()








