#!/usr/bin/env python
# -*- coding: utf-8 -*-

from irclib import IRC
from logger import Logger
from transport import Zero
from collections import OrderedDict

from settings import IRC_NETWORK
from settings import IRC_PORT
from settings import IRC_NICKNAME
from settings import IRC_USERNAME
from settings import IRC_IRCNAME
from settings import IRC_CHANNELS
from settings import HANDLERS_EVENTS


class Bot(IRC, object):

    network = IRC_NETWORK
    port = IRC_PORT
    nickname = IRC_NICKNAME
    username = IRC_USERNAME
    ircname = IRC_IRCNAME
    channels = IRC_CHANNELS

    def __init__(self):
        """
        constructor for IRC objects.
        creates and returns a ServerConnection object.
        """
        super(Bot, self).__init__()

    @property
    def _init(self):
        """
        init the freenode connection
        """
        Logger.log('{} connect on {}'.format(self.nickname, self.network), 'INFO')
        self._connection = self.server().connect(
            self.network,
            self.port,
            self.nickname,
            self.username,
            self.ircname,
        )
        return self._connection

    @property
    def _start(self):
        """
        loop
        add the zeroMQ publisher for sending events
        """
        self._connection.publisher = Zero().publisher
        Logger.log('process forever for {}'.format(self.nickname), 'INFO')
        while 1:
            self.process_once(1)

    @property
    def _disconnect(self):
        self.connection.disconnect()

    @property
    def _channels(self):
        for channel in self.channels:
            Logger.log('{} join {}'.format(self.nickname, channel), 'INFO')
            self._connection.join(channel)


class Events(object):

    events = HANDLERS_EVENTS

    @classmethod
    def subscribe2events(cls, connection):
        """
        Adds a global handler function for a specific event type
        """
        for event in cls.events:
            Logger.log('{} handle {} event'.format(connection.nickname, event), 'DEBUG')
            connection.add_global_handler(event, getattr(cls, "_on_" + event))

    @classmethod
    def recolt_event_informations(cls, event):
        """
        return all informations about an event from property
        """
        _informations = OrderedDict()
        for info in dir(event):
            if info.startswith('_') and not info.startswith('__'):
                _informations[info] = getattr(event, info)
        return _informations

    @classmethod
    def _on_join(cls, connection, event):
        """
        event - join the channel
        """
        infos = cls.recolt_event_informations(event)
        connection.publisher.send_json(infos)

    @classmethod
    def _on_part(cls, connection, event):
        """
        event - leave the channel
        """
        print "part"
        infos = cls.recolt_event_informations(event)
        connection.publisher.send_json(infos)

    @classmethod
    def _on_pubmsg(cls, connection, event):
        """
        event - message on the channel
        """
        infos = cls.recolt_event_informations(event)
        connection.publisher.send_json(infos)
