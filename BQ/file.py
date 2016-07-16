import mysql.connector
import re
import time

#打开数据库连接
db = mysql.connector.connect(host="192.168.88.150",user="root",password="root",database="spider")
#获取游标
cursor = db.cursor()

adict = {'玄幻小说列表':1,'修真小说列表':2,'都市小说列表':3,'历史小说列表':4,'网游小说列表':5,'科幻小说列表':6}
path = 'C:/Users/Administrator/Desktop/new.html'
file = open(path,'r',encoding='utf-8')
content = file.read()
re_catagory = re.compile('class="novellist"><h2>(.*?)</h2><ul>(.*?)</ul>', re.S)
catagory_retult = re.findall(re_catagory, content)
localtime = int(time.time())
if re_catagory:
    for catagory_page in catagory_retult:
        pattern = re.compile('<li><a href="/book/(.*?)/" target="_blank">(.*?)</a>(.*?)/(.*?)</li>', re.S)
        result = re.findall(pattern, catagory_page[1])
        if result:
            for item in result:
                if item[2].strip() == '(载)':
                    status = 1
                elif item[2].strip() == '(完)':
                    status = 2
                sql = "insert into sp_book (`sp_id`,`name`,`catagory`,`author`,`status`,`update_at`,`create_at`) values(%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql,[item[0].strip(),item[1].strip(),adict[catagory_page[0]],item[3].strip(),status,localtime,localtime])

file.close()
db.close()
