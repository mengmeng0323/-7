import requests
from bs4 import BeautifulSoup
import time
import random
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr



newTitle = ''

def getFirstTitle():
    response = requests.get('https://testerhome.com/topics/last')
    response.encoding = 'utf-8'
    firstTitle = \
        BeautifulSoup(response.text, 'lxml') \
            .find("div", class_="panel-body item-list") \
            .find("div", class_="title media-heading") \
            .find('a').get('title')
    return firstTitle
    # f = open("./html.txt")
    # return f.read()

def sendEmail(newTitle):

    my_sender = '2572309423@qq.com'  # 发件人邮箱账号
    my_user = 'ymhgh96@163.com'  # 收件人邮箱账号，我这边发送给自己
    try:
        f = open("./email.html", 'r', encoding='utf-8')
        content = f.read()
        content = content + "<div>" + newTitle + "</div></body></html>"
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

i = 1
while True:
    print('这是第' + str(i) + '次请求')
    i = i + 1
    firstTitle = getFirstTitle()
    if newTitle != firstTitle:
        res = sendEmail(firstTitle)
        if res:
            print('发送邮件也成功！')
            newTitle = firstTitle
        else:
            print('发送邮件失败！')
    time.sleep(random.randint(0, 5))
