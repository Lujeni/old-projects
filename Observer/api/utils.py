#/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from datetime import timedelta
from uuid import UUID

from flask import request
from flask import current_app
from werkzeug.exceptions import Unauthorized


def login_required(function):
    """ decorator that wraps http request for check authentication
    """
    def wrapper(*args, **kwargs):
        token = request.cookies.get('token', False)

        # mongoDB cursor
        tokens = current_app.mongo.observer.tokens

        # process
        if token:
            document = {
                'ttl': datetime.now() + timedelta(minutes=10),
            }

            token_document = current_app.mongo.magic(
                cursor=tokens,
                query={'_id': UUID(token)},
                update={'$set': document},
            )

            if token_document:
                return function(*args, **kwargs)
            else:
                raise Unauthorized('authentication required')
        else:
            raise Unauthorized('authentication required')
    return wrapper
