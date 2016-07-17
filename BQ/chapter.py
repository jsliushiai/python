import mysql.connector
import re
import time
import urllib.request

#打开数据库连接
db = mysql.connector.connect(host="192.168.88.150",user="root",password="root",database="spider")
#获取游标
cursor = db.cursor()

sql = "select * from sp_book where id > 4324"
cursor.execute(sql)
books = cursor.fetchall();

for book in books:
    baseUrl = 'http://www.biquge.la/book/' + str(book[1])
    bookName = book[3]
    id = book[0]
    try:
        rsp = urllib.request.urlopen(baseUrl)
    except:
        continue

    try:
        html = rsp.read().decode('gbk')
    except:
        continue

    pattern = re.compile('id="intro">(.*?)</p>', re.S)
    result = re.findall(pattern, html)
    try:
        desn = result[0].strip().strip('<p>')
    except:
        continue

    pattern = re.compile(bookName + '" src="(.*?)" width="120"', re.S)
    result = re.findall(pattern, html)
    try:
        pic = result[0].strip()
    except:
        continue


    localtime = int(time.time())

    sql = "update sp_book set desn = %s, cover_pic = %s, update_at = %s where id = %s"
    cursor.execute(sql, [desn, pic, localtime, id])

db.close()