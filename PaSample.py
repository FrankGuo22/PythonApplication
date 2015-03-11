# coding=utf-8
import urllib
import re
def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

def getImg(html):
	imglist = re.findall(r'.*src="(.+\.jpg)"',html)
	x = 0
	for imgurl in imglist:
		urllib.urlretrieve(imgurl,'D:\Frank Guo\Python\PythonPa\%s.jpg' % x)
		x += 1
	
html = getHtml("http://www.sina.com.cn/")
getImg(html)

