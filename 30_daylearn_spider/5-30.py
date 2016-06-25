# -*- coding: utf-8 -*-
# 爬出实践第五天之cookie的使用

import urllib2
import cookielib

def SaveCookie():
	cookie = cookielib.CookieJar()
	handler = urllib2.HTTPCookieProcessor(cookie)
	opener = urllib2.build_opener(handler)
	response = opener.open('http://baidu.com')
	for item in cookie:
		print 'Name='+item.name
		print 'Value='+item.value
	#将cookie保存到文件中
	filename = 'cookie.txt'
	cookie_file = cookielib.MozillaCookieJar(filename)
	cookie_file.save(ignore_discard=True, ignore_expires=True)

def GetCookie():
	#创建MozillaCookieJar实例对象
	cookie = cookielib.MozillaCookieJar()
	cookie.load('cookie.txt',ignore_discard=True, ignore_expires=True)
	req = urllib2.Request("http://www.zhihu.com")
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
	response = opener.open(req)
	print response.read()