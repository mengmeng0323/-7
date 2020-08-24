# -*- coding: utf-8 -*-
#  __author__:YM
#  2020/8/20

import MySQLdb

mydb = MySQLdb.connect(
    host='10.168.1.101',
    port=32673,
    user='m23100',
    password='123456',
    db='zentao',
    charset='utf8',
)
#创建游标
cur = mydb.cursor()
#查询
cur.execute("SELECT b.realname, COUNT(a.title) bug_num FROM zt_bug a left JOIN zt_user b on a.resolvedBy = b.account  WHERE a.`status` != 'active' GROUP BY b.realname ORDER BY COUNT(a.title) asc")
#获取表里数据
result = cur.fetchall()
print(result)