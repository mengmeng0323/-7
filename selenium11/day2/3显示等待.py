# -*- coding: utf-8 -*-
#  __author__:YM
#  2020/7/13
from selenium import webdriver
from selenium.webdriver.common.by import By  #设置元素定位选用哪种方法
from selenium.webdriver.support.ui import WebDriverWait  #提供等待方法类
from selenium.webdriver.support import expected_conditions as EC  #提供判断条件

driver = webdriver.Chrome('D:\software\selenium\chromedriver.exe')
#设置一个隐式等待     隐式等待和time.sleep互不相干


driver.get('http://www.baidu.com') #get 会等所有元素加载完成

driver.find_element_by_id('kw').send_keys('松勤\n')#\n相当于回车搜索的作用
#driver.find_element_by_link_text("松勤软件测试_腾讯课堂").click()
#每隔0.5秒检查一次，最多等待10秒,会返回元素对象
ele = WebDriverWait(driver,10,0.5).until(
    EC.visibility_of_element_located(
        (By.LINK_TEXT,"松勤软件测试_腾讯课堂")
    )
)
ele.click()
#driver.quit()

