# -*- coding: utf-8 -*-
import urllib

def  print_list(list):
    for i in list:
        print(i)

def demo():
    s = urllib.urlopen('http://douban.com')
    #print(s.read(100)) 读100字节
    '''
    for i in range(10): #打出行
        print('line %d: %s' % (i + 1, s.readline()))
    '''
    '''
    lines = s.readlines()
    print_list(lines)
    '''
    msq = s.info()
    print_list(msq.headers)
    print(msq.getheader('Content-Type'))
    print(s.getcode()) #200为成功应答
    print_list(dir(msq))
    print_list(msq.status)

def progress(blk, blk_size, total_size):
    print('%d/%d - %.02f%%' % (blk * blk_size, total_size, (float)(blk * blk_size) * 100 / total_size))

def retrieve():
    '''
    fname, msq = urllib.urlretrieve('http://douban.com', 'index.html')
    print(fname)
    print_list(msq.items())
    '''
    urllib.urlretrieve('http://blog.kamidox.com', 'index.html', reporthook=progress)


if __name__ == '__main__':
    '''demo()'''
    retrieve()
