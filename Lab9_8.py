import time
from selenium import webdriver
driver = webdriver.Chrome('D:\ki2nam3\KiemThuPhanMem\Chrome_Driver\chromedriver.exe')
driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/')
next1 =driver.find_element_by_xpath('//*[@id="content"]/ul/li[21]/a')
next1.click()
user_name = driver.find_element_by_id('username')
user_name.send_keys('tomsmith')
pass_word = driver.find_element_by_id('password')
pass_word.send_keys('SuperSecretPassword!')
btn_login = driver.find_element_by_css_selector("[class ='fa fa-2x fa-sign-in']")
btn_login.click()
title = driver.title
print(title)
time.sleep(2)
driver.close()