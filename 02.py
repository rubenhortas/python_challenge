# http://www.pythonchallenge.com/pc/def/ocr.html
import re

if __name__ == '__main__':
    rare_characters = re.compile('[a-zA-Z\\d ]', re.UNICODE)
    result = ""

    try:
        f = open('02_text.txt', 'r')

        for line in f.readlines():
            match = rare_characters.search(line)

            if match:
                result = "%s%s" % (result, match.group(0))

        f.close()
        print(result)
    except Exception as e:
        print(e)
