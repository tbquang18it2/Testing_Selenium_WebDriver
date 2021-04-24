from selenium import webdriver
import time
driver = webdriver.Chrome('D:\ki2nam3\KiemThuPhanMem\Chrome_Driver\chromedriver.exe')
driver.maximize_window()
driver.get('http://practice.automationtesting.in/')
time.sleep(2)
driver.quit()