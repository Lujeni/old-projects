#/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from datetime import timedelta
from json import dumps

from mimerender import FlaskMimeRender

from flask import Response

from werkzeug.exceptions import Unauthorized


def default_ressource_options(request, current_app):
    """ checks and manages all generic options for a ressource
    """
    ressource_options = {}
    ressource_options['callback'] = request.args.get('callback', False)
    ressource_options['token'] = request.cookies.get('token', False)
    ressource_options['query'] = request.args.get('q', False)
    return ressource_options


def setResponseCookies(response, token):
    """ Write the necessary cookies in the headers of the given response object
    """
    DOMAIN = "observer.thebault.co"

    if token:
        tenMinutes = datetime.utcnow() + timedelta(minutes=10)
        response.set_cookie(
            key='token',
            value=str(token),
            expires=tenMinutes.strftime("%a, %d-%b-%Y %H:%M:%S GMT"),
            domain=DOMAIN,
            httponly=True,
        )


def render_json(*args, **kwargs):
    """ render function for a given HTTP json header
    """
    content = {
        'count': 0,
        'data': None,
    }

    if 'exception' in kwargs:
        content['error'] = kwargs['exception'].message
    else:
        content['count'] = len(kwargs['data'])
        content['data'] = kwargs['data']

    # format content
    content = dumps(content)

    # jsonP
    if 'callback' in kwargs and kwargs['callback']:
        content = str(kwargs['callback']) + '(' + content + ')'

    # authentication
    if 'token' in kwargs and kwargs['token']:
        set_cookie_token = True
    else:
        set_cookie_token = False

    # prepare response
    response = Response(content)

    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Headers'] = 'Authorization, Content-Type, X-Requested-With'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
    # cache OPTIONS request
    response.headers['Access-Control-Max-Age'] = 1200

    # cookies
    if set_cookie_token:
        setResponseCookies(response, kwargs['token'])

    # return
    return response


mimerender = FlaskMimeRender()
# NOTE: decorator that wraps a HTTP request handle
decore_mimerender = mimerender(
    default='json',
    json=render_json,
)
# NOTE: decorator that wraps a HTTP exceptions handle
decore_mimerender_exceptions = mimerender.map_exceptions(
    mapping=(
        (AttributeError, '500 Internal Server Error'),
        (ValueError, '500 Internal Server Error'),
        (AttributeError, '500 Internal Server Error'),
        (KeyError, '500 Internal Server Error'),
        (IndexError, '500 Internal Server Error'),
        (TypeError, '500 Internal Server Error'),
        (Unauthorized, '401 Unauthorized'),
    ),
    default='json',
    json=render_json,
)
