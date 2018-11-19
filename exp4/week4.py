# -*- coding: UTF-8 -*-
import urllib2  
import sys  
 
class PaddingOracle(object):
    def __init__(self):
        self.targetURL = 'http://crypto-class.appspot.com/po?er='
    def query(self,q):
        target = self.targetURL +urllib2.quote(q)
        proxies = {"http": "127.0.0.1:1080", "https": "127.0.0.1:1080"}
        req = urllib2.Request(target)
        #req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36")
        try:
            f = urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            print "返回值" 
            print e
            return e.code == 404
def strxor(a, b):     # xor two strings of different lengths  
    if len(a) > len(b):  
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])  
    else:  
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])  

def attack():
    text = "f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb1".decode('hex')
    post = PaddingOracle()
    block = [[] for _ in range(4)]
    for i in range(4):
        block[i] = text[i*16:i*16+16]   #block store blocks
    find = []
    intermediary = [] #190, 134, 178, 72, 137, 190, 211, 102, 134, 176, 237, 211, 115, 32]
    #print intermediary 
    del block[2]
    del block[2]
    for i in reversed(range(1,4)):
        for j in reversed(range(16)):  #14
            edit_bit_num = 16 - j   #2
            old = list(block[0])   #2 - chunk
            k =15
            if intermediary != []:
                for x in intermediary:
                    old[k] = chr(edit_bit_num ^ x)
                    k -= 1
            for c in range(29,256):
                print '%d'%(c)
                old[j] = chr(c)       #16-2
                new = ''.join(old)
                block[0] = new
                #print list(block[0])
                if (post.query(''.join(block).encode("hex"))):
                    find.append(chr(c))            #找到这一位
                        #中间值
                    print "找到值%d"%(c)
                    intermediary.append(c^edit_bit_num)
                    break
                else:
                    continue
            print find
            print intermediary
        raw_input()
attack()

#The Magic Words are Squeamish Ossifrage									