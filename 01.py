#!/usr/bin/env python3
# _*_ coding:utf-8 _*

# http://www.pythonchallenge.com/pc/def/map.html
if __name__ == "__main__":
    text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
    trans = str.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")
    print(text.translate(trans))

    # Apply to the url
    text = "map"
    print("Apply to url: {0}".format(text.translate(trans)))
