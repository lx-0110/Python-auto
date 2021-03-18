# -*- coding: UTF-8 -*-
from selenium import webdriver
from time import sleep
from pywinauto.keyboard import send_keys

driver = webdriver.Chrome()
driver.get('https://kaifa.17mine.cn/#/login')
driver.maximize_window()
driver.implicitly_wait(10)   # 隐性等待10s

driver.find_element_by_xpath('//input[@name="telephone"]').clear()
driver.find_element_by_xpath('//input[@name="telephone"]').send_keys("xxwblx")
driver.find_element_by_xpath('//input[@name="password"]').clear()
driver.find_element_by_xpath('//input[@name="password"]').send_keys("123456")
sleep(10)
# 创建计磅单
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
driver.find_element_by_xpath('//input[@placeholder="请输入车牌"]').send_keys("津NLX999")
driver.find_element_by_xpath('//input[@placeholder="请输入毛重"]').send_keys("10")
driver.find_element_by_xpath('//input[@placeholder="请输入皮重"]').send_keys("0.1")
driver.find_element_by_xpath('//input[@placeholder="请输入扣重"]').send_keys("0.01")
driver.find_element_by_xpath('//input[@placeholder="请输入毛重称重时间"]').send_keys("2021-03-18")
driver.find_element_by_xpath('//input[@placeholder="请输入皮重称重时间"]').send_keys("2021-03-18")
driver.find_element_by_xpath('//td[text()="备注"]').click()
driver.find_element_by_xpath('//input[@placeholder="请输入毛重司磅员"]').send_keys("maozhong")
driver.find_element_by_xpath('//input[@placeholder="请输入皮重司磅员"]').send_keys("pizhong")
driver.find_element_by_xpath('//div[@class="upload_img_container"]/div[1]//div[@tabindex=0]').click()
sleep(2)
# driver.find_element_by_xpath('//div[@class="upload_img_container"]/div[1]//input[@type="file"]').send_keys(r'C:\\Users\SQM01\Desktop\1.png')
send_keys('C:\\Users\\SQM01\\Desktop\\1.png')
send_keys('{VK_RETURN}')

driver.find_element_by_xpath('//div[@class="upload_img_container"]/div[2]//div[@tabindex=0]').click()
sleep(2)
send_keys('C:\\Users\\SQM01\\Desktop\\1.png')
send_keys('{VK_RETURN}')

driver.find_element_by_xpath('//div[@class="upload_img_container"]/div[3]//div[@tabindex=0]').click()
sleep(2)
send_keys('C:\\Users\\SQM01\\Desktop\\1.png')
send_keys('{VK_RETURN}')

driver.find_element_by_xpath('//div[@class="upload_img_container"]/div[4]//div[@tabindex=0]').click()
sleep(2)
send_keys('C:\\Users\\SQM01\\Desktop\\1.png')
send_keys('{VK_RETURN}')
sleep(2)
driver.find_element_by_xpath('//span[text()="提交"]').click()

sleep(10)
driver.quit()
