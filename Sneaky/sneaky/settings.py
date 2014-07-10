#!/usr/bin/env python
# -*- coding: utf-8 -*-

from path import path
from random import randint

# DEBUG
DEBUG = False

# IRC bot
IRC_NETWORK = 'irc.freenode.com'
IRC_PORT = 6667
IRC_NICKNAME = '_Lujebot'
IRC_USERNAME = IRC_NICKNAME
IRC_IRCNAME = 'Lujeni bot'

if DEBUG:
    IRC_NICKNAME = IRC_NICKNAME + '-{}'.format(randint(1, 100))
    IRC_USERNAME = IRC_NICKNAME
IRC_CHANNELS = ['#python-bot', '#python-bot2', '#1000mercis']

# Handlers bot
HANDLERS_EVENTS = ["join", "part", "pubmsg"]

# Logger
LOG_LEVELS = {
    'DEBUG': 10,
    'INFO': 20,
    'WARNING': 30,
    'CRITICAL': 50
}
LOG_NAME = 'sneaky'
LOG_DIR = path('/tmp/')
LOG_FILE = LOG_DIR / 'sneaky.log'
LOG_CURRENT_LEVEL = LOG_LEVELS['DEBUG']
LOG_FORMAT = '%(asctime)s - %(message)s'

# MongoDB
MONGO_SERVER = '192.168.0.10:27017'
MONGO_DB = 'sneaky'

# ZeroMQ
if DEBUG:
    ZERO_PORT = 6666
else:
    ZERO_PORT = 5556
ZERO_BIND_ADDRESS = 'tcp://*:{}'.format(ZERO_PORT)
ZERO_CONNECT_ADDRESS = 'tcp://localhost:{}'.format(ZERO_PORT)
