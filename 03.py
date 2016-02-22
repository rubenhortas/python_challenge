#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    03  
"""

# http://www.pythonchallenge.com/pc/def/equality.html

import re

if __name__ == '__main__':
    small_letter = re.compile(
        '[^A-Z]+(?P<bodyguards1>[A-Z]{3})(?P<small_letter>[a-z]{1})(?P<bodyguards2>[A-Z]{3})[^A-Z]+', re.UNICODE)
    result = ""

    try:
        f = open('03_text.txt', 'r')

        for line in f.readlines():

            match = small_letter.search(line)
            if match:
                result = "{0}{1}".format(result, match.group("small_letter"))

        f.close()
        print result
    except Exception as e:
        print(e.message)
