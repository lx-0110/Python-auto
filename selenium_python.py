
# -*- coding: UTF-8 -*-
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://kaifa.17mine.cn/#/login')
driver.maximize_window()
sleep(10)

driver.find_element_by_xpath()
driver.find_element_by_id()

sleep(20)
driver.quit()
