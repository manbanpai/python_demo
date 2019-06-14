#coding:utf8

class UrlManage:

	def __init__(self):
		self.urls = set()
		self.disable = set()

	# 判断URL管理器中是否有数据
	def hasUrl(self):
		if len(self.urls) == 0:
			return
		return True

	# 取出一条URL
	def getUrl(self):
		if len(self.urls) == 0:
			return
		url = self.urls.pop()
		self.disable.add(url)
		return url

	# 批量添加URL
	def addUrls(self,urls):
		if urls is None:
			return
		for url in urls:
			self.addUrl(url)

	# 添加URL
	def addUrl(self,url):
		if url is None:
			return
		if url not in self.urls and url not in self.disable:
			self.urls.add(url) 