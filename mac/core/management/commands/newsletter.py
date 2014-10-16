# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand

from core.email import send_newsletter


class Command(BaseCommand):

    help = 'Send a newsletter'
    args = 'name, lang'

    def handle(self, *args, **kwargs):
        send_newsletter(*args)
