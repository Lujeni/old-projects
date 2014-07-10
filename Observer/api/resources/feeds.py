#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ast import literal_eval as eval

from flask import Blueprint
from flask import current_app
from flask import request
from flask.views import MethodView

from render import decore_mimerender
from render import decore_mimerender_exceptions
from render import default_ressource_options


class FeedsUtil(object):
    pass


class Feeds(MethodView):
    decorators = [decore_mimerender, decore_mimerender_exceptions]

    def get(self):
        ressource_options = default_ressource_options(request, current_app)
        cursor = current_app.mongo.feeds
        spec = {}
        # TODO: check the query
        if ressource_options['query']:
            spec = eval(ressource_options['query'])
        data = [feed for feed in cursor.find(spec=spec)]

        return dict({'data': data}, **ressource_options)

    # TODO: add a login required
    def put(self, feed_id):
        ressource_options = default_ressource_options(request, current_app)
        cursor = current_app.mongo.feeds
        put = dict(zip(request.form.keys(), request.form.values()))
        data = current_app.mongo.magic(
            cursor=cursor,
            query={'_id': feed_id},
            update={'$set': put},
            upsert=True,
        )
        return dict({'data': [data]}, **ressource_options)

    def options(self, feed_id=None):
        ressource_options = default_ressource_options(request, current_app)
        return dict({'data': ['options']}, **ressource_options)


view_feeds = Feeds.as_view('feeds')
feeds = Blueprint('feeds', __name__)
feeds.add_url_rule('/feeds', 'feeds', view_func=view_feeds, methods=['GET', 'OPTIONS'])
feeds.add_url_rule('/feeds/<string:feed_id>', 'feeds', view_func=view_feeds, methods=['GET', 'PUT', 'OPTIONS'])
