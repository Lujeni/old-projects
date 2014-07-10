#/usr/bin/env python
# -*- coding: utf-8 -*-
from re import match
from uuid import uuid4
from uuid import UUID
from datetime import datetime
from datetime import timedelta

from flask import Blueprint
from flask import current_app
from flask import request
from flask.views import MethodView

from render import decore_mimerender
from render import decore_mimerender_exceptions
from render import default_ressource_options

from werkzeug.exceptions import Unauthorized


class AuthUtils(object):

    @staticmethod
    def check_credentials_typo(credentials):
        """ basic checks for credentials
        """
        regex_username = r'^[\w\.\-]{2,}$'
        regex_password = r'[^.]{4,10}$'

        if not match(regex_username, credentials['username']):
            raise ValueError('invalid username typo')

        if not match(regex_password, credentials['password']):
            raise ValueError('invalid password typo')

    @staticmethod
    def check_credentials_validation(credentials):
        """ checks if the credentials match an valid user
        """
        spec = {'_id': credentials['username'], 'password': credentials['password']}
        if not current_app.mongo.observer.users.find_one(spec):
            raise Unauthorized('invalid credentials')

    @staticmethod
    def generate_token():
        """ generate random UUID for a token
        """
        return uuid4()


class Auth(MethodView):
    decorators = [decore_mimerender, decore_mimerender_exceptions]

    def get(self):
        """ handle authentication
        """
        ressource_options = default_ressource_options(request, current_app)
        token = ressource_options['token']
        valid_cookie_token = False

        # check if the token from cookie is valid
        if token and current_app.mongo.observer.tokens.find_one({'_id': UUID(token)}):
            valid_cookie_token = True

        # generate a new token
        if not token or not valid_cookie_token:
            credentials = request.authorization
            if not credentials:
                raise Unauthorized('empty authorization headers')

            AuthUtils.check_credentials_typo(credentials)
            AuthUtils.check_credentials_validation(credentials)

            token = AuthUtils.generate_token().hex
            document = {
                'ttl': datetime.now() + timedelta(minutes=10),
                'user': 'testing',
            }
            # NOTE: overwrite the bad token for the response cookies
            ressource_options['token'] = token

            current_app.mongo.magic(
                cursor=current_app.mongo.observer.tokens,
                query={'_id': UUID(token)},
                update={'$set': document},
                upsert=True,
            )

        return dict({'data': [{'token': token}]}, **ressource_options)

view_auth = Auth.as_view('auth')
auth = Blueprint('auth', __name__)
auth.add_url_rule('/auth/', 'auth', view_func=view_auth, methods=['GET'])
