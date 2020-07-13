import requests,re,platform
import datetime
from bs4 import BeautifulSoup
import smtplib


# newPage = ''
# def getPage():
#     response = requests.get('https://testerhome.com/topics/last')
#     response.encoding = 'utf-8'
#     page = \
#         BeautifulSoup(response.text, 'lxml')\
#         .find("div", class_="panel-body item-list")\
#         .find("div", class_="title media-heading")\
#         .find('a').get('title')
#     return page




#爬取详情
respon = requests.get('https://testerhome.com/topics/last')
respon.encoding = 'utf-8'
href = \
    BeautifulSoup(respon.text, 'lxml')\
    .find("div", class_="panel-body item-list")\
    .find("div", class_="title media-heading")\
    .find('a').get('href')
contentUrl = 'https://testerhome.com' + href


content = requests.get(contentUrl, timeout=5)
content.encoding = 'utf-8'
#传给解析器
content = BeautifulSoup(content.text, 'lxml').find("div",class_="col-md-9").get_text().strip()
print(content)

# while True:
#     page = getPage()
#     if newPage != page:
#         print('代替发邮件')











