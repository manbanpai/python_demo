#coding:utf8

from urllib import request
import ssl

class DownloadManage:

	def __enter__(self):
		return self

	def downimg(self,imgs):
		if imgs is None:
			return

		for img in imgs:
			path = img.split('/')
			newName = path.pop()
			resHtml = self.down(img)
		
			with open('D:/pythonCode/demo/spider/images/'+newName,'wb') as f:
				f.write(resHtml)


	def downhtml(self,url):
		content = self.down(url)
		content = content.decode('utf-8')
		return content

	def down(self,url):
		if url is None:
			return
		headers = {
			'User-Agent':r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                    	 r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
			'Referer':url,
			'Connection':'keep-alive'
		}
		req = request.Request(url,headers=headers)
		context = ssl._create_unverified_context()
		content = request.urlopen(req,context=context).read()
		return content

	def __exit__(self,exc_type,exc_value,traceback):
		print('DOWNLOAD')
		print(f'type:{exc_type}')
		print(f'type:{exc_value}')
		print(f'traceback:{traceback}')
		return True
		
