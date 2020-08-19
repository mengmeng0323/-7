# -*- coding: utf-8 -*-
#  __author__:YM
#  2020/7/22

from selenium import webdriver
import time

driver = webdriver.Chrome("D:\software\selenium\chromedriver.exe")
driver.get("http://www.baidu.com")
driver.get("http://news.baidu.com")

#浏览器后退
driver.back()
time.sleep(2)

#浏览器前进
driver.forward()
time.sleep(2)

#刷新界面
driver.refresh()
time.sleep(2)


'''
#参数数字为像素点
print("设置浏览器宽600，高600 显示")
driver.set_window_size(600,600)

time.sleep(2)

#设置为全屏显示
driver.maximize_window()
'''
