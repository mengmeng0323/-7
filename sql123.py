import pymysql
db = pymysql.connect(host='localhost',user='root',passwd='root',db='python')

cursor = db.cursor()

sql = '''insert into ym_spider(title,content) values ('大家好','哈哈哈哈1')'''

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()