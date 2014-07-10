#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
from sys import exit
from sys import argv
# TODO: use the standard librarys
try:
    from clint.textui import colored
except ImportError:
    print('need the client module (https://pypi.python.org/pypi/clint/)')


# TODO: replace by an config parser
parser = {
    'default': 'black',
    'uwsgi': 'blue',
    'ssh': 'red',
    'rtg': 'green',
}


class Pretty(object):

    def __init__(self, _file):
        try:
            # TODO: check the file
            self.file_cursor = open(_file, 'r')
            self.file_cursor.seek(0, 2)
            self.parser_keys = parser.keys()
        except IOError as e:
            print('{}'.format(e))
            exit(1)

    def display(self, line):
        # TODO: can color line or word
        _line = line.replace('\n', '\t')
        color = parser['default']
        for key in self.parser_keys:
            if key in _line:
                color = parser[key]
                break
        _colored = getattr(colored, color)
        print(_colored(_line))

    @property
    def read_forever(self):
        while True:
            cursor_place = self.file_cursor.tell()
            line = self.file_cursor.readline()
            if not line:
                sleep(0.5)
                self.file_cursor.seek(cursor_place)
            else:
                self.display(line)

if __name__ == '__main__':
    # TODO: can use argparse instead of config parser
    if not len(argv) > 1:
        print('specify a file')
        exit(0)

    pretty = Pretty(argv[1])
    pretty.read_forever
