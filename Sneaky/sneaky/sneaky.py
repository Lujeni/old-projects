#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bot import Bot
from bot import Events
from logger import Logger


def main():
    Logger.init()

    server = Bot()
    freenode = server._init

    # join channels
    server._channels

    # add events on the freenode connection
    Events.subscribe2events(freenode)

    # process_forever the bot
    server._start

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
