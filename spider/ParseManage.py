#coding:utf8
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class ParseManage:

	def parse(self,url,content):
		if content is None or url is None:
			return

		soup = BeautifulSoup(content,'html.parser')

		imgs = self.getImgs(url,soup)
		urls = self.getUrlList(url,soup)
		return imgs,urls

	def getImgs(self,url,soup):
		imgs = set()
		links = soup.find_all('img',src=True)
		for link in links:
			fullUrl = urljoin(url,link['src'])
			imgs.add(fullUrl)
		return imgs

	def getUrlList(self,url,soup):
		urls = set()
		links = soup.find_all('a',href=True)
		for link in links:
			fullUrl = urljoin(url,link['href'])
			urls.add(fullUrl)
		return urls

	def __enter__(self):
		return self

	def __exit__(self,exc_type,exc_value,traceback):
		if exc_type is not None:
			print('PARSE')
			print(f'type:{exc_type}')
			print(f'type:{exc_value}')
			print(f'traceback:{traceback}')
		return True

