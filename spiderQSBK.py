#-*- coding: utf-8 -*-
import urllib
import urllib2
import re
import thread
import time

#糗事百科爬虫类
class spiderQSBK:
	#初始化
	def __init__(self):
		self.pageIndex = 1
		self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
		#初始化headers
		self.header = {'User-Agent' : self.user_agent }
		self.stories = []
		self.enable = False
	#抓取html	
	def getPage(self, pageIndex):
		try:
			url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
			req = urllib2.Request(url,headers = self.header)
            #利用urlopen获取页面代码
			rsp = urllib2.urlopen(req)
            #将页面转化为UTF-8编码
			pageContent = rsp.read().decode('utf-8')
			return pageContent
		except urllib2.URLError, e:
			if hasattr(e,"reason"):
				print u"连接糗事百科失败,错误原因",e.reason
				return None
	#regex html	
	def getPageItems(self,pageIndex):
		pageContent = self.getPage(pageIndex)
		if not pageContent:
			print "页面加载失败....."
			return None
		pattern = re.compile('h2>(.*?)</h2.*?content">(.*?)</div>(.*?)<div class="st.*?number">(.*?)</',re.S)
		items = re.findall(pattern,pageContent)
		pageStories = []
		for item in items:
			hasImg = re.search('img',item[2])
			if not hasImg:
				replaceBR = re.compile('<br/>')
				text = re.sub(replaceBR,'\n',item[1])
				pageStories.append([item[0].strip(),text.strip(),item[3].strip()])
		return pageStories
	#add self.stories	
	def loadPage(self):
		if self.enable == True:
			if len(self.stories) < 2:
				pageStories = self.getPageItems(self.pageIndex)
				if pageStories:
					self.stories.append(pageStories)
					self.pageIndex += 1
	
	#交互
	def getOneStory(self,pageStories,page):
		for story in pageStories:
			input = raw_input()
			self.loadPage()
			if input == 'Q':
				self.enable = False
				return
			print u"第%d页\t发布人:%s\t赞:%s\n%s" %(page,story[0],story[2],story[1])

	#start
	def start(self):
		print u"正在读取糗事百科,按回车查看新段子，Q退出"
		self.enable = True
		self.loadPage()
		nowPage = 0
		while self.enable:
			if len(self.stories) > 0:
				pageStories = self.stories[0]
				nowPage += 1
				del self.stories[0]
				self.getOneStory(pageStories,nowPage)


				
spider = spiderQSBK()
spider.start()




	
