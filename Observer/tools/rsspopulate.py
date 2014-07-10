#/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time
import feedparser

from bson.objectid import ObjectId
from datetime import datetime
from md5 import new as md5_new
from multiprocessing import Process
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from pymongo.errors import DuplicateKeyError

__all__ = ['Populate']


class DocPrinter(dict):

    def __setitem__(self, key, value):
        """ pretty display for mongoDB document
        """
        if isinstance(value, datetime):
            value = value.strftime('%Y-%m-%d %H:%M:%S')

        elif isinstance(value, ObjectId):
            value = value.generation_time.strftime('%Y-%m-%d %H:%M:%S')

        dict.__setitem__(self, key, value)


class MongoDB(object):

    def __init__(self):
        try:
            self.mongo = MongoClient(
                host='192.168.0.10',
                document_class=DocPrinter,
                connectTimeoutMS=3000,
            )
            self.observerDB = self.mongo['observer']
            self.rssCol = self.observerDB['rss']
            self.feedsCol = self.observerDB['feeds']
        except ConnectionFailure as error:
            sys.stdout.write('{}\n'.format(error))
            sys.exit(1)

    @property
    def getRSS(self):
        """ retrieve the list of RSS
        """
        return [rss for rss in self.rssCol.find()]

    def storeFeeds(self, url, feeds):
        """ store all feeds in database
        """
        for feed in feeds:
            _date = time.localtime()
            if 'published_parsed' in feed:
                _date = feed['published_parsed']
            date = datetime(_date.tm_year, _date.tm_mon, _date.tm_mday)
            doc = {
                '_id': md5_new(feed.id).hexdigest(),
                'title': feed.title,
                'date': date,
                'link': feed.link,
                'summary': feed.summary,
                'type': url,
                'status': 'new',
            }
            try:
                self.feedsCol.insert(doc)
            except DuplicateKeyError:
                pass


class Populate(MongoDB):

    def __init__(self):
        super(Populate, self).__init__()
        self.rss_list = self.getRSS

    def retrieveFeed(self, rss_url):
        """ retrieve the list of feeds for a specific RSS
        """
        url = 'http://{}'.format(rss_url)
        result = feedparser.parse(url)
        if result.status != 200:
            sys.stdout.write('request failed for retrieve this RSS ({})\n'.format(url))
        else:
            self.storeFeeds(url, result['items'])

if __name__ == '__main__':
    populate = Populate()
    for rss in populate.rss_list:
        p = Process(
            target=populate.retrieveFeed,
            args=(rss['url'],),
        )
        p.start()
    # wait the last process
    p.join()
    exit(0)
