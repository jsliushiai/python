# -*- coding:utf-8 -*-  
#import urllib2

#res = urllib2.urlopen("http://www.baidu.com")
#print res.read()

#req = urllib2.Request("http://www.baidu.com")
#res = urllib2.urlopen(req)
#print res.read()

#POST方式
#import urllib
#import urllib2

#value = {"username":"250358333@qq.com","password":"123456"}
#value = {}
#value['username'] = "250358333@qq.com"
#value['password'] = '123456'
#data = urllib.urlencode(value)
#url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
#GET方式
#url = "https://passport.csdn.net/account/login"
#geturl = url + "?" + data
#req = urllib2.Request(url,geturl)
#res = urllib2.urlopen(req)
#print res.read()

#import urllib
#import urllib2

#url = 'https://passport.csdn.net/account/login'
#user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#value = {'username':'cqc','passwd':'123456'}
#header = {'User-Agent':user_agent,'Referer':'http://www.zhihu.com/articles'}
#data = urllib.urlencode(value)
#req = urllib2.Request(url,data,header)
#res = urllib2.urlopen(req)
#page = res.read()
#print page

#dubuglog
#import urllib2
#httpHandler = urllib2.HTTPHandler(debuglevel=1)
#httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
#opener = urllib2.build_opener(httpHandler, httpsHandler)
#urllib2.install_opener(opener)
#response = urllib2.urlopen('http://www.baidu.com')


#URLError
#import urllib2

#req = urllib2.Request("http://www.xxxxxx.com")
#try:
#	urllib2.urlopen(req)
#except urllib2.URLError,e:
#	print e.reason

#HTTPError
#import urllib2

#req = urllib2.Request('http://blog.csdn.net/cqcre')
#try:
#	urllib2.urlopen(req)
#except urllib2.HTTPError, e:
#	print e.code
#	print e.reason

#import urllib2
#import cookielib

#cookie = cookielib.CookieJar()
#save cookie in file
#filename = 'cookie.txt'
#cookie = cookielib.MozillaCookieJar(filename)
#handle = urllib2.HTTPCookieProcessor(cookie)
#opener = urllib2.build_opener(handle)

#res = opener.open("http://www.baidu.com")
#for item in cookie:
#	print 'Name = '+item.name
#	print 'Value = '+item.value
#save cookie in file
#cookie.save(ignore_discard=True, ignore_expires=True)










