#!/usr/bin/env python3
# _*_ coding:utf-8 _*

# http://www.pythonchallenge.com/pc/def/ocr.html
import re

if __name__ == "__main__":
    rare_characters = re.compile("[a-zA-Z0-9 ]", re.UNICODE)
    result = ""

    try:
        f = open("02_text.txt", "r")

        for line in f.readlines():
            match = rare_characters.search(line)

            if match:
                result = "{0}{1}".format(result, match.group(0))

        f.close()
        print(result)
    except Exception as e:
        print(e)
