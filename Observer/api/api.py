#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import path
from site import addsitedir
from socket import gethostname

from flask import Flask

from bdd import MongoDB

current_directory = path.dirname(path.realpath(__file__))
addsitedir(current_directory)

##############################################################################
hostname = gethostname()
debug = True if not 'python' in hostname else True
api = Flask(__name__)
api.mongo = MongoDB()

# resources
# TODO: generic import
from rss import rss
from auth import auth
from feeds import feeds

api.register_blueprint(rss)
api.register_blueprint(auth)
api.register_blueprint(feeds)

##############################################################################
if __name__ == '__main__':
    api.run(host='0.0.0.0', port=80, debug=True)
