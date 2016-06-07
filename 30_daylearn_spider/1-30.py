# -*- coding: utf-8 -*-

import urllib2
from pip._vendor.requests.api import request
#30天爬去指定qq号qq空间
def SpiderDemo1():
    # urlopen(url, data, timeout)
    # 第一个参数url即为URL，第二个参数data是访问URL时要传送的数据，第三个timeout是设置超时时间。
    # 第二三个参数是可以不传送的，data默认为空None，timeout默认为 socket._GLOBAL_DEFAULT_TIMEOUT
    # 第一个参数URL是必须要传送的，在这个例子里面我们传送了百度的URL，执行urlopen方法之后，返回一个response对象，返回信息便保存在这里面。
    response = urllib2.urlopen("http://qzone.qq.com/")
    print response.read()
def SpiderDemo2():
#     构建请求时还需要加入好多内容，通过构建一个request，服务器响应请求得到应答，这样显得逻辑上清晰明确。
    request = urllib2.Request("http://www.baidu.com")
    response = urllib2.urlopen(request)
    print response.read()

if __name__=="__main__":
   SpiderDemo1()
   SpiderDemo2()
   a = [1,2,2,3,4,4,5,6,78,3]
   b = [4,5,66,3,2,3,4,2,3,7]
   
