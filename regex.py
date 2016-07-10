#-*- coding: utf-8 -*-
__author__ = '刘世爱'

#导入模块  
import re

pattern = re.compile(r'hello')

result1 = re.match(pattern,'hello')
result2 = re.match(pattern,'helloo mo,eo!')
result3 = re.match(pattern,'helo mo,eo!')
result4 = re.match(pattern,'hello mo,eo!')

if result1:
	print result1.group()
else:
	print '1匹配失败'

if result2:
	print result1.group()
else:
	print '2匹配失败'

if result3:
	print result1.group()
else:
	print '3匹配失败'

if result4:
	print result1.group()
else:
	print '4匹配失败'
