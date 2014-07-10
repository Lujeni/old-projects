#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: user MongoClient
from pymongo import Connection
from pymongo.errors import ConnectionFailure
from pymongo.errors import DuplicateKeyError
from pymongo.errors import InvalidName
from logger import Logger

from settings import MONGO_SERVER
from settings import MONGO_DB


class Mongo(object):

    server = MONGO_SERVER
    database = MONGO_DB

    def __init__(self):
        try:
            self.server = Connection(self.server)
            self.sneakyDB = self.server[self.database]
            Logger.log('connection to mongoDB', 'DEBUG')
        except ConnectionFailure, e:
            Logger.log('unable to connect on mongoDB {}'.format(e), 'WARNING')
            pass

    def insert(self, collection, document):
        try:
            self.sneakyDB[collection].insert(document)
        except DuplicateKeyError, e:
            Logger.log('{}'.format(e), 'WARNING')
            pass
        except InvalidName, e:
            self.sneakyDB['defaults'].insert(document)
            Logger.log('insert empty collection ({})'.format(e), 'WARNING')
        except NameError, e:
            Logger.log('discarding invalid insert ({})'.format(e), 'WARNING')
            pass
