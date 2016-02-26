#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    05  
"""

# http://www.pythonchallenge.com/pc/def/peak.html

import urllib2
import pickle
import signal
from handlers.python import exit_signal_handler

if __name__ == '__main__':

    signal.signal(signal.SIGINT, exit_signal_handler)

    try:
        str = ''

        response = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
        data = pickle.load(response)
        response.close()

        for l in data:  # data composed of lists
            for t in l:  # lists composed by tuples
                str = '{0}{1}'.format(str, (t[1] * t[0]))
            str = '{0}\n'.format(str)

        print str

    except Exception as e:
        print(e.message)
