# -*- coding: utf-8 -*-
#  __author__:YM
#  2020/8/18

# coding=utf-8

import MySQLdb
from jinja2 import Template



def getData (sql):
    # 打开数据库连接
    db = MySQLdb.connect(
        host='10.168.1.101',  # 主机名
        port=32673,  # 端口号(默认的)
        user='m23100',  # 用户名
        passwd='123456',  # 密码
        db='zentao',  # 数据库名
        charset='utf8',  # 编码
    )
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        # 关闭数据库连接
        db.close()
        return results
    except Exception:
        print(Exception)


#获取每个人的总bug数
sql = "SELECT b.realname, COUNT(a.title) bug_num FROM zt_bug a left JOIN zt_user b on a.resolvedBy = b.account  WHERE a.`status` != 'active' GROUP BY b.realname ORDER BY COUNT(a.title) asc"
allUserAllBug = getData(sql)
sql = "SELECT COUNT(title) all_bug_num FROM zt_bug WHERE `status` != 'active'"
allBug = getData(sql)[0][0]

f = open("./model.html", 'r', encoding='utf-8')
content = f.read()

#利用模板引擎替换对应位置变量
tableData = []
template = Template(content)
for row in allUserAllBug:
    preValue = round(row[1]/allBug * 100, 2)
    emoji = 0
    if preValue > 10:
        emoji = 1

    tableData.append({
        'name': row[0],
        'bug_num': row[1],
        'pre': str(preValue) + '%',
        'emoji': emoji,
        'pre_num': preValue
    })
# 把每次得到的newTitle赋给newTitle
print(tableData)

content = template.render(tableData=tableData)

sendHtml = open('index.html', 'w', encoding="utf-8")
sendHtml.write(content + "\n\n")
sendHtml.close()

#print(allUserAllBug)
