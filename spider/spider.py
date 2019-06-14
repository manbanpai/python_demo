#coding:utf8
import UrlManage,DownloadManage,ParseManage

class Spider:

	def __init__(self,url):
		# 初始化URL管理器
		self.urlManage = UrlManage.UrlManage()
		# 将出事话URL放入URL管理器
		self.urlManage.addUrl(url)

	def work(self,num=1000):
		count = 0
		# 判断URL管理器中是否有数据
		while self.urlManage.hasUrl():
			# 从URL管理器中取出一个URL
			url = self.urlManage.getUrl()		
			# 将URL交给下载器 返回CONTENT
			with DownloadManage.DownloadManage() as download:
				content = download.downhtml(url)
			# 将CONTENT交给页面解析器 返回图片列表和URL列表
			with ParseManage.ParseManage() as parse:
				imgs,urls = parse.parse(url,content)
			# 将图片列表交给图片下载器
			with DownloadManage.DownloadManage() as download:
				content = download.downimg(imgs)
			# 将URL列表交给URL管理器
			self.urlManage.addUrls(urls)
			# 最大执行次数
			if count == num:
				break
			count = count+1

	def __enter__(self):
		return self

	def __exit__(self,exc_type,exc_value,traceback):
		print('SPIDER')
		print(f'type:{exc_type}')
		print(f'type:{exc_value}')
		print(f'traceback:{traceback}')
		return True


if __name__ == '__main__':
	url = "";
	with Spider(url) as spider:
		spider.work(1)