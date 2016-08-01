import mysql.connector
import re
import time
import urllib.request

page = 4630
#打开数据库连接
db = mysql.connector.connect(host="192.168.88.150",user="root",password="root",database="spider")
#获取游标
cursor = db.cursor()

for index in range(1,page+1):
    baseUrl = 'http://bbs.tianya.cn/m/post-worldlook-223829-'+str(index)+'.shtml'
    try:
        res = rsp = urllib.request.urlopen(baseUrl)
    except:
        continue

    try:
        html = rsp.read().decode('utf-8').strip()
    except:
        continue
		
    #正则楼主了
    pattern = re.compile('item item-ht item-lz(.*?)<div class="ft">', re.S)
    result = re.findall(pattern, html)

    for item in result:
        if item:
            #发表时间和楼层
            pattern = re.compile('data-time="(.*?)" data-id="(.*?)">', re.S)
            menu = re.findall(pattern, item)
            if menu:
                timeStr = menu[0][0]
                timeArray = time.strptime(timeStr, "%Y-%m-%d %H:%M")
                # 转换为时间戳:
                times = int(time.mktime(timeArray))
                floor = menu[0][1]
            else:
                times = 0
                floor = 0
            #正文
            patterns = re.compile('<div class="bd">(.*?)</div>', re.S)
            contents = re.findall(patterns, item)
            if contents:
                content = contents[0].strip()
            else:
                content = ''

            localtime = int(time.time())

            #入库
            sql = "insert into sp_tianya (`time`,`content`,`createtime`,`floor`) values(%s,%s,%s,%s)"
            cursor.execute(sql, [times, content, localtime,floor])
        else:
            continue

    print(index)

db.close()