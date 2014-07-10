#!/usr/bin/env python
# -*- coding: utf-8 -*-

from transport import Zero
from logger import Logger
from storage import Mongo


def main():
    subscriber = Zero().subscriber
    sneaky_mongo = Mongo()
    while True:
        message = subscriber.recv_json()
        if message:
            Logger.log("worker process message: {}".format(message), 'DEBUG')
            channel = message.pop('_target').replace('#', '').replace('-', '_')
            sneaky_mongo.insert(channel, message)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
