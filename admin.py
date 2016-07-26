#coding:utf-8
import os,sys
import tornado.ioloop
import tornado.web
from tornado.escape import json_encode


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            "index.html",
            apis = apis
        )


application = tornado.web.Application(
    handlers = [
      (r'/',MainHandler)
    ],
    template_path = os.path.join(os.path.dirname(__file__),'templates'),
    static_path = os.path.join(os.path.dirname(__file__),'public'),
    debug = True
)
