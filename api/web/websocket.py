# coding: UTF-8

from error import Error
import json
import os
import tornado.locale
from dotenv import load_dotenv, find_dotenv
import tornado.web
import tornado.websocket

load_dotenv(find_dotenv())

class WebSocket(tornado.websocket.WebSocketHandler, tornado.web.RequestHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(message)

    def on_close(self):
        print("WebSocket closed")

    def post(self):
        # load translations
        tornado.locale.load_translations('locale')

        # set translation
        _ = tornado.locale.get('es').translate

        # parse post data
        data = json.dumps({ k: self.get_argument(k) for k in self.request.arguments })

        # error class
        error = Error()

        # verify access_token

        try:
            access_token = self.get_argument('access_token', '')
            if access_token == os.getenv('ACCESS_TOKEN'):
                self.write_message(data)

                self.write(data)
            else:
                error.error = _("Invalid access token")
                error_object = json.dumps(error.__dict__)
                self.write(error_object)
        except KeyError, e:
            error.error = _("Access token is required")
            error_object = json.dumps(error.__dict__)
            self.write(error_object)
