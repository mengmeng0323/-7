# -*- coding: utf-8 -*-
#  __author__:YM
#  2020/8/21
import time
import requests

#获取当前时间
def get_time2():
    return time.time()

#获取接口信息
def webapi(url):
    resp = requests.get(url)
    return resp.text