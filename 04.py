#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    04  
"""

# http://www.pythonchallenge.com/pc/def/linkedlist.php

import re
import signal
import urllib2

from handlers.python import exit_signal_handler
from handlers.url import print_html

BASE_URL = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
CHAIN_RE = re.compile('(nothing[a-zA-Z =]*)(?P<next>[0-9]*)')


def get_url(i, url):
    try:
        print '{0} - Fetching {1}'.format(i, url)

        response = urllib2.urlopen(url)
        html = response.read()

        match = CHAIN_RE.search(html)
        if match:
            next_url = "{0}{1}".format(BASE_URL, match.group('next'))
            get_url(i + 1, next_url)
        else:
            print_html(html)

    except Exception as e:
        print e.message


if __name__ == '__main__':
    signal.signal(signal.SIGINT, exit_signal_handler)

    get_url(0, "http://www.pythonchallenge.com/pc/def/linkedlist.php")  # 86 calls
    get_url(0, "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022")  # 164 calls
