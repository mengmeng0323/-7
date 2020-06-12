import requests
import sys
from bs4 import BeautifulSoup


import MySQLdb
#mydb = MySQLdb.connect(host='localhost',user='root',passwd='root',db='python')
mydb = MySQLdb.connect('localhost','root','root','python',charset='utf8')
cursor = mydb.cursor()


f = open('spider.txt', 'w', encoding="utf-8")

i = 1
while i < 8:
     #print('当前读取到：' + str(i) + "页面 \n\n")
     listPage = requests.get('https://www.chu.edu.cn/xxgk/1617/list' + str(i) + '.htm')
     listPage.encoding = 'utf-8'
     html = BeautifulSoup(listPage.text, 'lxml').find("div",id="wp_news_w3")
     aList = BeautifulSoup(str(html), 'lxml').find_all("a")

     for a in aList:
          #print(a.get_text())
          #新闻标题
          #f.write(a.get_text() + "\n\n")
          #开始访问详情页
          href = a.get('href')
          contentUrl = 'https://www.chu.edu.cn' + href
          if href.find("http") != -1:
              contentUrl = href
          try:
              content = requests.get(contentUrl, timeout=5)
              content.encoding = 'utf-8'
             #传给解析器
              content = BeautifulSoup(content.text, 'lxml').find("div",class_="Article_Content")
              #新闻内容
              #f.write(content.get_text() + "\n\n\n")
              #sql = '''insert into ym_spider(title, content) values ('" + a.get_text() + "','" + content.get_text() + "')'''
              #sql = '''insert into ym_spider(title,content) values ("''' + a.get_text() + '''","'''+content.get_text()+'''")'''
              sql = '''insert into ym_spider(title,content) values('%s','%s')'''%(a.get_text(),content.get_text())
              f.write(sql + "\n\n")
              try:
                  print(sql)
                  cursor.execute(sql)
                  mydb.commit()
                  print('导入数据库成功')
              except Exception as e:
                  mydb.rollback()
                  print('失败' + str(e))
              #sys.exit();
          except Exception as e:
              print('捕获到了一个错误页面，跳过当前页面不在执行！' + str(e))
     i += 1
     print('\n')
cursor.close()




