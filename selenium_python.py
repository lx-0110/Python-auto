# -*- coding: UTF-8 -*-
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://kaifa.17mine.cn/#/login')
driver.maximize_window()
sleep(10)

driver.quit()
