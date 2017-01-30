# coding: UTF-8

import app.web

urls = [
    (r'/',  app.web.Home),
    (r'/websocket',  app.web.WebSocket),
]
