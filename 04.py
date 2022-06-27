#!/usr/bin/env python3
# http://www.pythonchallenge.com/pc/def/linkedlist.php
import re
import signal

from urllib import request
from handlers.python import exit_signal_handler
from handlers.url import print_html

BASE_URL = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
CHAIN_RE = re.compile('(nothing[a-zA-Z =]*)(?P<next>\\d*)')


def get_url(i, url):
    try:
        print(f"{i} - Fetching {url}")

        response = request.urlopen(url)
        html = response.read()
        match = CHAIN_RE.search(str(html, 'utf-8'))

        if match:
            next_url = f"{BASE_URL}{match.group('next')}"
            get_url(i + 1, next_url)
        else:
            print_html(str(html, 'utf-8'))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, exit_signal_handler)

    get_url(0, "http://www.pythonchallenge.com/pc/def/linkedlist.php")  # 86 calls
    get_url(0, "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022")  # 164 calls
