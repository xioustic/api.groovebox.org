#!/usr/bin/env pythonNone
#-*-coding: utf-8 -*-

"""
    app.py
    ~~~~~~    

    :copyright: (c) 2015 by Mek
    :license: see LICENSE for more details.
"""

from flask import Flask
from flask.ext.routing import router
import views
from views import apis
from configs import options

urls = ('/api', apis,
        '/q/<code>/<name>', views.Playlist,
        '/q/<code>', views.Playlist,
        '/favicon.ico', views.Favicon,
        '/<path:uri>', views.Base,
        '/', views.Base
        )
app = router(Flask(__name__), urls)

if __name__ == "__main__":
    app.run(**options)
