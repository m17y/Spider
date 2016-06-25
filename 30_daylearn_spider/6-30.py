# -*- coding: utf-8 -*-
# 爬出实践第六天之模拟登录qq空间
import urllib2
import urllib
import cookielib

def LoginQzone(): 
	filename = 'qzoneCookie.txt'
	cookie = cookielib.MozillaCookieJar(filename)
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
	postdata = urllib.urlencode({
				'u':'100714131',
				'p':'1994'
		})
	login_url = 'http://qzone.qq.com/' 
	result = opener.open(login_url,postdata)
	#保存cookie到cookie.txt中
	cookie.save(ignore_discard=True, ignore_expires=True)
	#利用cookie请求访问另一个网址，此网址是成绩查询网址
	next_url = 'xxx'
	result = opener.open(next_url)
	"""
	创建一个带有cookie的opener，在访问登录的URL时，
	将登录后的cookie保存下来，然后利用这个cookie来访问其他网址。
	"""