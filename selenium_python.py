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
driver.find_element_by_xpath('//li[@class="tabs-item active-tab"]').click()
driver.find_element_by_xpath('//span[text()="创建"]').click()
driver.find_element_by_xpath('//span[text()="订单编号："]/following-sibling::div//input[@placeholder="请输入"]').send_keys('DD20210309000002')
driver.find_element_by_xpath('//span[text()="经理人手机号："]/parent::div//div[@title="请选择"]').click()
driver.find_element_by_xpath('//div[text()="刘欣外部经理人"]').click()
driver.find_element_by_xpath('//span[text()="确 定"]').click()
driver.find_element_by_xpath('//span[text()="收款账户："]/following-sibling::div').click()
driver.find_element_by_xpath('//label[@class="el-radio"]').click()
driver.find_element_by_xpath('//span[text()="确定"]').click()

sleep(10)
driver.quit()
