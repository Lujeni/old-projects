#/usr/bin/env python
# -*- coding: utf-8 -*-
from re import match

from flask import Blueprint
from flask import current_app
from flask import request
from flask.views import MethodView

from render import decore_mimerender
from render import decore_mimerender_exceptions
from render import default_ressource_options


class RssUtils(object):
    """ docstrings
    """
    @staticmethod
    def validate_rss_name(rss_name):
        """ simply validation before mongoDB query
        """
        regex = r'^[\w]+$'
        if not match(regex, str(rss_name)):
            raise ValueError('invalid rss name ({})'.format(rss_name))


class Rss(MethodView):
    """ docstrings
    """
    decorators = [decore_mimerender, decore_mimerender_exceptions]

    def get(self, rss_name=None):
        """ retrieve the list of a rss
        """
        ressource_options = default_ressource_options(request, current_app)
        if rss_name:
            RssUtils.validate_rss_name(rss_name)
            spec = {'name': {'$regex': rss_name}}
        else:
            spec = {}

        results = current_app.mongo.finder(
            cursor=current_app.mongo.rss,
            spec=spec
        )
        data = [document for document in results]
        return dict({'data': data}, **ressource_options)

    def post(self):
        """ add a new rss
            @post data:
                <name>
                <url>
        """
        ressource_options = default_ressource_options(request, current_app)
        #TODO: validate post data
        new_rss = dict(zip(request.form.keys(), request.form.values()))
        if current_app.mongo.observer.rss.find_one({'name': new_rss['name']}):
            raise ValueError('document already exists')

        data = current_app.mongo.magic(
            cursor=current_app.mongo.observer.rss,
            query={'name': new_rss['name']},
            update=new_rss,
            upsert=True
        )
        return dict({'data': [data]}, **ressource_options)

    def patch(self, rss_name):
        """ patch a rss for the givent rss_name parameter
            @patch data:
                <name>
                <url>
        """
        ressource_options = default_ressource_options(request, current_app)
        #TODO: validate patch data
        patch_rss = dict(zip(request.form.keys(), request.form.values()))
        data = current_app.mongo.magic(
            cursor=current_app.mongo.observer.rss,
            query={'name': rss_name},
            update={'$set': patch_rss},
        )
        return dict({'data': [data]}, **ressource_options)

view_rss = Rss.as_view('rss')
rss = Blueprint('rss', __name__)
rss.add_url_rule('/rss', 'rss', view_func=view_rss, methods=['GET', 'POST'])
rss.add_url_rule('/rss/<string:rss_name>', 'rss', view_func=view_rss, methods=['GET', 'PATCH'])
