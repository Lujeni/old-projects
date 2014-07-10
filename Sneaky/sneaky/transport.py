#!/usr/bin/env python
# -*- coding: utf-8 -*-

from logger import Logger
from sys import exit

from zmq import Context
from zmq import SUB
from zmq import PUB
from zmq import SUBSCRIBE
from zmq import ZMQError

from settings import ZERO_CONNECT_ADDRESS
from settings import ZERO_BIND_ADDRESS


# TODO: use greenlets: import zmq.green as zmq
# TODO: use socket options for publisher: SNDHWM, LINGER
class Zero(object):

    def __init__(self):
        self.context = Context()

    @property
    def subscriber(self):
        try:
            self._subscriber = self.context.socket(SUB)
            self._subscriber.bind(ZERO_BIND_ADDRESS)
            self._subscriber.setsockopt(SUBSCRIBE, "")
        except ZMQError as error:
            Logger.log('E200: {}'.format(error), 'CRITICAL')
            exit(200)
        except Exception as error:
            Logger.log('E201: {}'.format(error), 'CRITICAL')
            exit(201)
        else:
            Logger.log('bind subscriber on {}'.format(ZERO_BIND_ADDRESS), 'DEBUG')
            return self._subscriber

    @property
    def publisher(self):
        try:
            self._publisher = self.context.socket(PUB)
            self._publisher.connect(ZERO_CONNECT_ADDRESS)
        except ZMQError as error:
            Logger.log('E202: {}'.format(error), 'CRITICAL')
            exit(202)
        except Exception as error:
            Logger.log('E203: {}'.format(error), 'CRITICAL')
            exit(203)
        else:
            Logger.log('connection publisher on {}'.format(ZERO_CONNECT_ADDRESS), 'DEBUG')
            return self._publisher

    @property
    def destroy(self):
        self._subscriber.close()
        self._publisher.close()
        self.context.destroy()
        Logger.log('destroy zmq socket', 'DEBUG')
