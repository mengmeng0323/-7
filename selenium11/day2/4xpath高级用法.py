# -*- coding: utf-8 -*-
#  __author__:YM
#  2020/7/14

'''
xpath 使用路径表达式来选取HTML  文档中的节点、或节点集
'''
from selenium import webdriver

#创建一个浏览器驱动对象
driver = webdriver.Chrome('D:\software\selenium\chromedriver.exe')
#访问网址
driver.get('file:///D:/software/pycharm/-7/selenium11/test.html')