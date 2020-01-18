from selenium import webdriver
from time import time

driver = webdriver.Chrome()
driver.get("http://www.wsb.pl")
driver.maximize_window()
sleep(5)
driver.close()
