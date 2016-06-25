# -*- coding: utf-8 -*-
# URL异常处理

import urllib2
def SpiderDemo():
	url = "http://qzone.qq.com/"
	user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
	value = {'u':'name','p':'password'}
	header = {'User-Agent':user_agent}
	data = urllib2.urlencode(value)
	request = urllib2.Request(url,data,header)
	try:
		response = urllib2.urlopen(request)
		page = response.read()
		return page
	except urllib2.URLError,e:
		return e.reason

if __name__=="__main__":
	print SpiderDemo()