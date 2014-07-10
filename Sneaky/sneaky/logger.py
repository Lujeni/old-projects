#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from sys import exit

from settings import LOG_LEVELS
from settings import LOG_NAME
from settings import LOG_FILE
from settings import LOG_CURRENT_LEVEL
from settings import LOG_FORMAT


class Logger:

    log_levels = LOG_LEVELS
    log_name = LOG_NAME
    log_file = LOG_FILE
    log_level = LOG_CURRENT_LEVEL
    log_format = LOG_FORMAT

    @classmethod
    def init(cls, level=None, file=None):
        try:
            log_level = level if level else cls.log_level
            log_file = file if file else cls.log_file

            cls.logger = logging.getLogger(cls.log_name)
            cls.logger.setLevel(log_level)

            fh = logging.FileHandler(log_file)
            formatter = logging.Formatter(cls.log_format, datefmt="%Y-%m-%d")

            fh.setFormatter(formatter)
            cls.logger.addHandler(fh)
        except IOError as error:
            print "E100: {}".format(error)
            exit(100)
        except Exception as error:
            print "E101: {}".format(error)
            exit(101)

    @classmethod
    def log(cls, message, message_level=None):
        """Process a log.

        Keyword arguments:
        message - the message <string>
        message_level - optionnal level <string> (DEBUG)
        """
        try:
            if not hasattr(cls, 'logger'):
                Logger.init()

            if not message_level:
                level = cls.logger.level
            else:
                level = cls.log_levels[message_level.upper()]
            cls.logger.log(level, message)
        except Exception as error:
            print "E102: {}".format(error)
            pass
