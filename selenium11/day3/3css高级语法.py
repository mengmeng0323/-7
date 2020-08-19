# -*- coding: utf-8 -*-
#  __author__:YM
#  2020/7/23

from selenium import webdriver
import time

driver = webdriver.Chrome("D:\software\selenium\chromedriver.exe")
#访问网址
driver.get("http://www.baidu.com")