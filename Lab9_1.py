import time
from selenium import webdriver
driver = webdriver.Chrome('D:\ki2nam3\KiemThuPhanMem\Chrome_Driver\chromedriver.exe')
driver.get('http://practice.automationtesting.in/')
time.sleep(2)
driver.quit()