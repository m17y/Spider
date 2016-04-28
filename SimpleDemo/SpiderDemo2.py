# -*- coding: utf-8 -*-

import urllib2
import urllib
from pip._vendor.requests.api import request
from _socket import timeout
#用POST和GET数据传送
def SpiderDemo():
#     我们需要定义一个字典，名字为values，参数我设置了username和password，
#     下面利用urllib的urlencode方法将字典编码，命名为data，
#     构建request时传入两个参数，url和data，运行程序，即可实现登陆，
    
    values = {"username":"100714131@qq.com","password":"xxx"}
    data = urllib.urlencode(values)
    url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
    request = urllib2.Request(url,data)
#     timeout 超时设置
    response = urllib2.urlopen(request,timeout=10)
    print response.read()
    
#     import urllib2
#  
#     values={}
#     values['username'] = "1016903103@qq.com"
#     values['password']="XXXX"
#     data = urllib.urlencode(values) 
#     url = "http://passport.csdn.net/account/login"
#     geturl = url + "?"+data
#     request = urllib2.Request(geturl)
#     response = urllib2.urlopen(request)
#     print response.read()

#添加agent就是请求的身份
def SpiderDemo1():
    url = 'http://www.server.com/login'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
    values = {'username' : 'cqc',  'password' : 'XXXX' }  
    #添加agent就是请求的身份
    headers = { 'User-Agent' : user_agent }  
    data = urllib.urlencode(values)  
    request = urllib2.Request(url, data, headers)  
    response = urllib2.urlopen(request)  
    page = response.read() 
    
    #对付反盗链
#     headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  ,
#                         'Referer':'http://www.zhihu.com/articles' }  
#    将heard 传入request中
def ProxySpider():
    enable_proxy = True
    proxy_header = urllib2.ProxyHandler({"http":"http://some-proxy.com:8080"})
    null_proxy_handler = urllib2.ProxyHandler({})
    if enable_proxy:
        opener = urllib2.build_opener(proxy_header)
    else:
        opener = urllib2.build_opener(null_proxy_handler)
    urllib2.install_opener(opener)

# 开启debug    
def DebugSpider():
    httpHandler = urllib2.HTTPHandler(debuglevel=1)
    httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
    opener = urllib2.build_opener(httpHandler, httpsHandler)
    urllib2.install_opener(opener)
    response = urllib2.urlopen('http://www.baidu.com')

if __name__=="__main__":
#    SpiderDemo()
#    SpiderDemo1()
   DebugSpider()
# headers的一些属性
# User-Agent : 有些服务器或 Proxy 会通过该值来判断是否是浏览器发出的请求
# Content-Type : 在使用 REST 接口时，服务器会检查该值，用来确定 HTTP Body 中的内容该怎样解析。
# application/xml ： 在 XML RPC，如 RESTful/SOAP 调用时使用
# application/json ： 在 JSON RPC 调用时使用
# application/x-www-form-urlencoded ： 浏览器提交 Web 表单时使用
# 在使用服务器提供的 RESTful 或 SOAP 服务时， Content-Type 设置错误会导致服务器拒绝服务