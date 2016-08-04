fr = open("C:/Users/365/Desktop/mysqlstatus_2016-08-03.log",encoding="UTF-8")
fw = open("F://2016-08-03.txt",mode='a',encoding="UTF-8")

item = 815808
for line in fr:
    contnet = line.strip().split(' ')
    qps = int(contnet[0]) - int(item)
    item = contnet[0]
    result = str(qps)+','+contnet[1]+','+contnet[2]+','+contnet[3]+','+contnet[4]
    fw.write(result+"\n")
    
fr.close()
fw.close()
