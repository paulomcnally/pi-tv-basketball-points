# coding: UTF-8

import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.autoreload
import os

tornado.options.define("port", default=8000, help="run on the given port", type=int)

from urls import urls

class ServerApp(tornado.web.Application):
    def __init__(self):
        settings = {
        'debug': True,
        'static_path': os.path.join('./', 'static')
        }

        tornado.web.Application.__init__(self,handlers = urls,**settings)

def runServer():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(ServerApp())
    http_server.listen(tornado.options.options.port)
    instance = tornado.ioloop.IOLoop.instance()
    tornado.autoreload.start(instance)
    instance.start()

if __name__ == "__main__":
    runServer()
