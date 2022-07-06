#!/usr/bin/env python3

# http://www.pythonchallenge.com/pc/def/ocr.html

import re

if __name__ == '__main__':
    # re = re.compile('[a-zA-Z.,:;''\\d ]', re.UNICODE) # Book characters
    re = re.compile('[a-z]', re.UNICODE)  # Needed characters to solve the challenge
    result = ""

    try:
        f = open('02_text.txt', 'r')

        for line in f.readlines():
            match = re.search(line)

            if match:
                result = f"{result}{match.group(0)}"

        f.close()
        print(result)
    except Exception as e:
        print(e)
