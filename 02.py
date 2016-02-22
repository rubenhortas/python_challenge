#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    02.py  
"""

# http://www.pythonchallenge.com/pc/def/ocr.html

import re

if __name__ == '__main__':
    rare_characters = re.compile('[a-zA-Z0-9 ]', re.UNICODE)
    result = ""

    try:
        f = open('02_text.txt', 'r')

        for line in f.readlines():
            match = rare_characters.search(line)
            if match:
                result = "{0}{1}".format(result, match.group(0))

        f.close()

        print result

    except Exception as e:
        print(e.message)
