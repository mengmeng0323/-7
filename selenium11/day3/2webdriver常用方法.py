# -*- coding: utf-8 -*-
#  __author__:YM
#  2020/7/23
from selenium import webdriver
import time

driver = webdriver.Chrome("D:\software\selenium\chromedriver.exe")
#访问网址
driver.get("http://www.baidu.com")

'''
#模拟按键输入，针对input标签进行的操作
time.sleep(2)
driver.find_element_by_id("kw").send_keys("selenium")
time.sleep(2)
#单击元素
driver.find_element_by_id("su").click()
time.sleep(2)
#清空文本
driver.find_element_by_id("kw").clear()
'''

"""
ele = driver.find_element_by_id("kw")
ele.send_keys("python")
ele.submit()
"""

#text 获取元素的文本
eleText = driver.find_element_by_xpath("//div[@class=\"title-text c-font-medium c-color-t\"]").text
print(eleText)

#get_attribute 获得属性值
ele = driver.find_element_by_id("virus-2020")
print(ele.get_attribute("target"))

# is_displayed 检测元素是否可见
ele = driver.find_element_by_id("s_is_result_css")
print(ele.is_displayed())


time.sleep(5)
driver.quit()