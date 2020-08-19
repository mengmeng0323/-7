import requests
from bs4 import BeautifulSoup
import time
import random
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from jinja2 import Template

# f = open("./email.html", 'r', encoding='utf-8')
# content = f.read()
# print(content)
# template = Template(content)
# print (template.render(name='John Doe'))

def getFirstTitle():
    response = requests.get('https://testerhome.com/topics/last') #拿到网页地址给response
    response.encoding = 'utf-8'
    #找到标题对应的a标签
    a = BeautifulSoup(response.text, 'lxml') \
            .find("div", class_="panel-body item-list") \
            .find("div", class_="title media-heading") \
            .find('a')
    #创建一个空字典，用于存放title和href
    firstContent = {}
    firstContent['title'] = a.get('title')
    firstContent['href'] = a.get('href')
    #返回两个值1
    return firstContent
    # f = open("./html.txt")
    # return f.read()

def getArticle(href):
    response = requests.get(href)
    response.encoding = 'utf-8'
    article = BeautifulSoup(response.text, 'lxml') \
        .find("div", class_="panel-body markdown markdown-toc")  #拿到文章内容
    return article

def sendEmail(newTitle, href):

    my_sender = '2572309423@qq.com'  # 发件人邮箱账号
    my_user = 'ymhgh96@163.com'  # 收件人邮箱账号，我这边发送给自己
    try:
        f = open("./email.html", 'r', encoding='utf-8')
        content = f.read()

        #利用模板引擎替换对应位置变量
        template = Template(content)
        article = getArticle(href)
        # 把每次得到的newTitle赋给newTitle
        content = template.render(newTitle=newTitle, article=article)

        smtpObj = smtplib.SMTP_SSL('smtp.qq.com', 465)
        smtpObj.login(my_sender, 'vpstivazakiqdigb')

        msg = MIMEText(content, 'html', 'utf-8')
        msg['From'] = formataddr(["FromRunoob", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号

        nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        msg['Subject'] = "叶萌的监控软件提示---当前时间：" + nowTime

        smtpObj.sendmail(my_sender, [my_user, ], msg.as_string())
        return True
    except Exception:
        return False

oldTitle = ''
i = 1
while True:
    print('这是第' + str(i) + '次请求')
    i = i + 1
    firstContent = getFirstTitle()
    #如果老的标题跟新的标题不一样，就要发送邮件  并且会把新的标题替换旧标题
    if oldTitle != firstContent['title']:
        res = sendEmail(firstContent['title'], 'https://testerhome.com' + firstContent['href'])
        if res:
            print('发送邮件也成功！')
            oldTitle = firstContent['title']
        else:
            print('发送邮件失败！')
    time.sleep(random.randint(0, 5))  #如果标题一样就休眠随机5秒之内再循环
