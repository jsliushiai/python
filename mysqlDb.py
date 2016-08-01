#-*- coding: utf-8 -*-
__author__ = '刘世爱'

import mysql.connector
#打开数据库连接
db = mysql.connector.connect(host="192.168.88.150",user="root",password="root",database="book")
#获取游标
cursor = db.cursor()
#执行sql语句
cursor.execute("select version()")
#获得一条记录
data = cursor.fetchone()

print ("Database version: %s" %data)
#关闭数据库连接
db.close()