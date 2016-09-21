# -*- coding: utf-8 -*-

import urllib2
import urllib
from pip._vendor.requests.api import request
import cookielib

def BlogSpider():
# 简单的爬我的Blog
    filename  = "D:/cookie.txt"
    cookie = cookielib.MozillaCookieJar(filename)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    postdata = urllib.urlencode({'log':'su',
                                 'pwd':'root'}
                                )

if __name__=="__main__":
   BlogSpider()
   
