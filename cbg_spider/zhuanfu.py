#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.ioloop
import tornado.web
import json
import urllib2

class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        print "setting headers!!!"
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def options(self, *args, **kwargs):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

class IndexHandler(BaseHandler):
    def get(self):
        zone_name = self.get_argument('zone_name')
        request = urllib2.Request("http://xyq.163.com/2011/zhuanyi/js/travel_list.js")
        response = urllib2.urlopen(request)

        data = response.read()
        data = json.loads(data[12:])
        zone_data = data.get(zone_name)
        zone_data_sw = {}
        for k,v in data.items():
            if (zone_name in v):
                print bool(k==zone_name)
                zone_data_sw[k] = v
        self.write(dict(zone_data_sw=zone_data_sw,zone_data=zone_data))

settings = {

    'template_path': 'views',
    'static_path': 'static',
    'static_url_prefix': '/static/',
}

application = tornado.web.Application([
    (r"/", IndexHandler),

], **settings)

if __name__ == "__main__":
    application.listen(1994)
    tornado.ioloop.IOLoop.instance().start()