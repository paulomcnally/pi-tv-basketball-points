# coding: UTF-8

import tornado.web

class Home(tornado.web.RequestHandler):
    def get(self):
        self.render("../../templates/template.html", title="Puntos")
