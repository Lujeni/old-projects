#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import exit
from sys import stdout
from bson.objectid import ObjectId
from datetime import datetime

from gevent import monkey
monkey.patch_all()
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


__all__ = ['MongoDB']


class DocPrinter(dict):

    def __setitem__(self, key, value):
        """ pretty display for mongoDB document
        """
        if isinstance(value, datetime):
            value = value.strftime('%Y-%m-%d')

        elif isinstance(value, ObjectId):
            value = value.generation_time.strftime('%Y-%m-%d %H:%M:%S')

        dict.__setitem__(self, key, value)


class MongoDB(object):

    def __init__(self):
        """ init the mongoDB connection
        """
        try:
            self.mongo = MongoClient(
                host='192.168.0.10',
                document_class=DocPrinter
            )
            self.observer = self.mongo.observer
            self.rss = self.observer.rss
            self.feeds = self.observer.feeds
        except ConnectionFailure as error:
            stdout.write('{}\n'.format(error))
            exit(1)

    def finder(self, cursor, spec, options={}):
        """ generic find
            return: cursor query
        """
        return cursor.find(
            spec=spec,
            **options
        )

    def magic(self, cursor, query, update, upsert=False, remove=False, full_response=False, new=True, **options):
        """ generic find and modify
            return: the document updated
        """
        return cursor.find_and_modify(
            query=query,
            update=update,
            upsert=upsert,
            remove=remove,
            full_response=full_response,
            new=new,
            **options
        )
