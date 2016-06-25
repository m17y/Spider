# -*- coding: utf-8 -*-
#30天学习爬虫实践
import urllib2
def SpiderDemo():
	url = "http://qzone.qq.com/"
	user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
	value = {'u':'name','p':'password'}
	header = {'User-Agent':user_agent}
	data = urllib2.urlencode(value)
	request = urllib2.Request(url,data,header)
	response = urllib2.urlopen(request)
	page = response.read()
	return page
#对付”反盗链” headers中加入referer 
#headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  ,
#                        'Referer':'http://www.zhihu.com/articles' }  

if __name__=="__main__":
	print SpiderDemo()