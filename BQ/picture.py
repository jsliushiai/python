import mysql.connector
import re
import time
import urllib.request
import os
import math

#保存图片
def saveFile(path,fileName,data):
    if data == None:
        return None

    mkdir(path)

    file = open(path + fileName, "wb")
    file.write(data)
    file.flush()
    file.close()

#生成目录
def mkdir(path):
    path = path.strip()

    if not os.path.exists(path):
        os.makedirs(path)

    return path

#打开数据库连接
db = mysql.connector.connect(host="192.168.88.150",user="root",password="root",database="spider")
#获取游标
cursor = db.cursor()

sql = "select id,sp_id,cover_pic from sp_book "
cursor.execute(sql)
books = cursor.fetchall();

for book in books:
    try:
        baseUrl = book[2]
        id = book[0]
        sp_id = book[1]
    except:
        continue

    try:
        ext = os.path.splitext(baseUrl)
        tmp = math.floor(sp_id / 1000)
        fileName = str(sp_id) + 's' + ext[1]
        path = r'./files/cover/' + str(tmp) + '/'
    except:
        continue

    try:
        req = urllib.request.urlopen(baseUrl)
        buf = req.read()
    except:
        continue

    try:
        saveFile(path, fileName, buf)
    except:
        continue

    localtime = int(time.time())
    sql = "update sp_book set cover_pic = %s, update_at = %s where id = %s"
    cursor.execute(sql, [path+fileName, localtime, id])

db.close()

