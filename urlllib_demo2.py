# -*- coding: UTF-8 -*-
import urllib
import urlparse

def urlencode():
    params = {'score': 100, 'name': '爬虫基础', 'comment': 'very good'}
    qs = urllib.urlencode(params)
    print(qs)
    print(urlparse.parse_qs(qs))
#
# def parse_qs():
#

if __name__ == '__main__':
    urlencode()