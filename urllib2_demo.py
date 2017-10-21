# -*- coding: utf-8 -*-
import urllib2
# import urllib
import cookielib

'''
def urlopen():
    url = 'http://blog.kamidox.com/no-exist'
    try:                                    # 捕获错误
        s = urllib2.urlopen(url, timeout=3) #超时
    except urllib2.HTTPError, e:
        print(e)                            #不存在网页打印出404
    else:
        print(s.read(100))
        s.close()
'''

'''
def request():
    headers = {'User-Agent': 'Mozilla/5.0', 'x-my-header': 'my value'}
    req = urllib2.Request('http://blog.kamidox.com', headers=headers)
    s = urllib2.urlopen(req)
    # print(s.read(100)) 打印头
    print(req.headers)
    s.close()
'''

'''
def request_post_debug():
    # POST
    data = {'username': 'kamidox', 'password': 'xxxxxxxx'}
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request('http://www.douban.com', data=urllib.urlencode(data), headers=headers)
    opener = urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1))
    s = opener.open(req)
    print(s.read(200))
    s.close()
'''
def handle_cookie():
    cookiejar = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookiejar=cookiejar)
    opener = urllib2.build_opener(handler, urllib2.HTTPSHandler(debuglevel=1))
    s = opener.open('https://www.zhihu.com')
    print(s.read(100))
    s.close()

    print ('=' *80)
    print(cookiejar._cookies)
    print('=' * 80)

    s = opener.open('https://www.zhihu.com')
    s.close()


if __name__ == "__main__":
    # urlopen()
    # request()
    # request_post_debug()
    handle_cookie()
