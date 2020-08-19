# -*- coding: utf-8 -*-
#  __author__:YM
#  2020/8/18

import MySQLdb

mydb = MySQLdb.connect('10.168.1.101','m23100','123456','python',charset='utf8')
cur = mydb.cursor()
cur.execute("select")
