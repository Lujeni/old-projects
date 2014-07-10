#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import zmq
sys.path.append('/home/julien/github/perso/Sneaky/sneaky')
sys.path.append('/root/github/Sneaky/sneaky')

import unittest
import settings
import logging
import pymongo
import time

from path import path
from logger import Logger
from transport import Zero
from storage import Mongo


class TestLogger(unittest.TestCase):

    def setUp(self):
        self.logfile = path(settings.LOG_FILE)

    def test_init(self):
        Logger.init()
        self.assertTrue(isinstance(Logger.logger, logging.Logger))
        self.assertTrue(self.logfile.isfile())
        self.assertEquals(Logger.logger.level, settings.LOG_CURRENT_LEVEL)
        self.assertEquals(Logger.logger.name, settings.LOG_NAME)

    def test_arguments(self):
        # level
        Logger.init(level=50)
        self.assertEquals(Logger.logger.level, 50)
        del Logger.logger
        Logger.init(level=-1)
        self.assertEquals(Logger.logger.level, -1)
        del Logger.logger
        # 0 level is impossible
        Logger.init(level=0)
        self.assertEquals(Logger.logger.level, settings.LOG_CURRENT_LEVEL)
        del Logger.logger

        # file
        Logger.init(file='/tmp/unittest.log')
        self.assertTrue(path('/tmp/unittest.log').isfile())
        del Logger.logger

    def tearDown(self):
        try:
            del Logger.logger
            self.logfile.remove()
        except Exception:
            pass


class TestTransport(unittest.TestCase):

    def setUp(self):
        self.zero = Zero()
        self._pub = self.zero.publisher
        self._sub = self.zero.subscriber

    def test_context(self):
        self.assertIsInstance(self.zero.context, zmq.Context)

    def test_socket_type(self):
        self.assertEquals(self._pub.socket_type, 1)
        self.assertEquals(self._sub.socket_type, 2)

    def test_ping_pong(self):
        json = {'ping': 'pong'}
        self._pub.send_json(json)
        message1 = self._sub.recv_json()
        self.assertDictEqual(json, message1)

        json = {'pong': 'ping'}
        self._pub.send_json(json)
        message2 = self._sub.recv_json()
        self.assertDictEqual(json, message2)

    def test_term(self):
        self.zero.destroy
        self.assertTrue(self._pub.closed)
        self.assertTrue(self._sub.closed)
        self.assertTrue(self.zero.context)

    def tearDown(self):
        self.zero.destroy


class TestMongo(unittest.TestCase):

    def setUp(self):
        self.mongo = Mongo()
        self.host, self.port = settings.MONGO_SERVER.split(':')

    def test_arguments(self):
        self.assertTrue(hasattr(self.mongo, 'sneakyDB'))
        self.assertIsInstance(self.mongo.sneakyDB, pymongo.database.Database)
        self.assertSequenceEqual(self.mongo.server.host, self.host)
        self.assertSequenceEqual(str(self.mongo.server.port), self.port)
        self.assertTrue(self.mongo.server.is_primary)

    def test_insertion(self):
        unit_col = 'unittest'
        unit_json = {'unit_key': 'unit_value'}

        self.mongo.insert(unit_col, unit_json)
        for doc in self.mongo.sneakyDB[unit_col].find(spec=unit_json):
            time.sleep(0.5)
            self.assertDictEqual(unit_json, doc)
        self.mongo.sneakyDB[unit_col].drop()

        # bad collection
        self.mongo.insert('**oups', unit_json)
        for doc in self.mongo.sneakyDB['default'].find(spec=unit_json):
            time.sleep(0.5)
            self.assertDictEqual(unit_json, doc)
        self.mongo.sneakyDB[unit_col].drop()

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
