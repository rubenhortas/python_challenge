# http://www.pythonchallenge.com/pc/def/peak.html

import pickle
import signal

from urllib import request
from handlers.python import exit_signal_handler

if __name__ == "__main__":
    signal.signal(signal.SIGINT, exit_signal_handler)

    try:
        s = ""
        response = request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
        data = pickle.load(response)
        response.close()

        for ld in data:  # data composed of lists
            for t in ld:  # lists composed by tuples
                s = "{0}{1}".format(s, (t[1] * t[0]))

            s = "{0}\n".format(s)

        print(s)
    except Exception as e:
        print(e)
