# http://www.pythonchallenge.com/pc/def/channel.html

import signal

from zipfile import ZipFile
from handlers.python import exit_signal_handler


# noinspection PyShadowingNames
def get_next_file(i, zf, file_name, result):
    is_last = True

    try:
        file_words = zf.read(file_name).split()
        info = zf.getinfo(file_name).comment

        result = f"{result}{info}"

        for word in file_words:
            if word.isdigit():
                is_last = False
                next_file = f"{word.decode('utf-8')}.txt"
                get_next_file(i + 1, zf, next_file, result)

        if is_last:
            print(result)
    except Exception as e:
        raise e


if __name__ == '__main__':
    signal.signal(signal.SIGINT, exit_signal_handler)

    result = ""

    # Download the zip file from http://www.pythonchallenge.com/pc/def/channel.zip
    try:
        with ZipFile('channel.zip') as zf:
            get_next_file(0, zf, 'readme.txt', result)
    except Exception as e:
        print(e)
