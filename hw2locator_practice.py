from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()




# by XPATH(amazon logo, need help)
driver.find_element(By.XPATH, "//a[@class='a-icon a-icon-logo']")
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# BY class using x path
driver.find_element(By.XPATH, " *[@class = 'icp-new-nav-flag']")




# search box and continue button
driver.find_element(By.ID, 'ap_email')
driver.find_element(By.ID, 'continue')

# Condition of use
driver.find_element(By.XPATH, "a[@herf='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")



