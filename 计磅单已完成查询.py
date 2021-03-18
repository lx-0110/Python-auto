# -*- coding: UTF-8 -*-
from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.get('https://kaifa.17mine.cn/#/login')
driver.maximize_window()
driver.implicitly_wait(10)   # 隐性等待10s

driver.find_element_by_xpath('//input[@name="telephone"]').clear()
driver.find_element_by_xpath('//input[@name="telephone"]').send_keys("xxwblx")
driver.find_element_by_xpath('//input[@name="password"]').clear()
driver.find_element_by_xpath('//input[@name="password"]').send_keys("123456")
sleep(10)

driver.find_element_by_xpath('//button[@type="button"]').click()
driver.find_element_by_xpath('//span[text()="采购管理"]').click()
driver.find_element_by_xpath('//li[@tabindex="-1"]/span[text()="计磅单管理"]').click()
driver.find_element_by_xpath('//li[text()="已完成"]').click()

#按照供货单号搜索
driver.find_element_by_xpath('//label[text()="供货单号"]/parent::div//input').send_keys("0312000002")
driver.find_element_by_xpath('//span[text()="搜索"]').click()
sleep(5)
driver.find_element_by_xpath('//span[text()="重置"]').click()
##选择料型，并按照料型搜索##
driver.find_element_by_xpath('//label[text()="采购料型"]/parent::div//input').click()
driver.find_element_by_xpath('//span[text()="中型"]').click()
driver.find_element_by_xpath('//span[text()="中废A"]').click()
driver.find_element_by_xpath('//span[text()="搜索"]').click()
sleep(5)
driver.find_element_by_xpath('//span[text()="重置"]').click()

#按照计磅日期搜索 自己选择了一个固定的时间段
driver.find_element_by_xpath('//label[text()="计磅日期"]/parent::div//input[@placeholder="起始日期"]').click()
driver.find_element_by_xpath('//div[@class="el-picker-panel__content el-date-range-picker__content is-left"]//span[text()=12]').click()
driver.find_element_by_xpath('//div[@class="el-picker-panel__content el-date-range-picker__content is-left"]//span[text()=18]').click()
sleep(2)
driver.find_element_by_xpath('//span[text()="搜索"]').click()
sleep(5)
driver.find_element_by_xpath('//span[text()="重置"]').click()

sleep(5)
# driver.quit()