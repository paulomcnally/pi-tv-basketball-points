# coding: UTF-8

import tornado.websocket
import tornado.web
import tornado.ioloop
import json
import os
from dotenv import load_dotenv, find_dotenv
from error import Error
load_dotenv(find_dotenv())

# WebSocket
class WebSocket(tornado.websocket.WebSocketHandler, tornado.web.RequestHandler):

    # connections array
    connections = set()

    # alow local origin
    def check_origin(self, origin):
        return True

    # add connection
    def open(self):
        self.connections.add(self)
        print("WebSocket opened")

    # write message
    def on_message(self, message):
        self.write_message(message)

    # remove connection
    def on_close(self):
        self.connections.remove(self)
        print("WebSocket closed")

    # to send messages from server
    # require and http post
    # @url: /websocket
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
            # load access_token from body param
            access_token = self.get_argument('access_token', '')

            # compare body with environment variable
            if access_token == os.getenv('ACCESS_TOKEN'):

                # each connections and write message
                [con.write_message(data) for con in self.connections]

                # ouput body
                self.write(data)
            else:
                # show error - Invalid access token
                error.error = _("Invalid access token")
                error_object = json.dumps(error.__dict__)
                self.write(error_object)
        except KeyError, e:
            # show error - Access token is required
            error.error = _("Access token is required")
            error_object = json.dumps(error.__dict__)
            self.write(error_object)
