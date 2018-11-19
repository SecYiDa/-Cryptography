
# -*- coding: UTF-8 -*-
from Crypto.Cipher import AES
from random import randint
from base64 import b64decode
def exp1(block):
    padding_len = 16 -  (len(block)%16)
    #print chr(19)
    return block + chr(padding_len) * padding_len

def exp2():
    def aes_ecb(data,key):                #AES ecb
        cipher = AES.new(key, AES.MODE_ECB)
        return cipher.encrypt(data)
    def xor_str(x, y):
        return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(x, y))
    def cbc(data,key,iv):
        result = ''
        old = iv
        for i in range(0,len(data),16):
            new  = data[i:i+16]
            old = aes_ecb(xor_str(old,new), key)
            result += old
        return result
    f = open('10.txt', 'r')
    data = f.read().decode('base64')
    print cbc(data,"YELLOW SUBMARINE", '\x00' * 16)

def exp3(data):
    def randkey():                                                  #rand key
        return ''.join(chr(randint(0,255)) for i in range(16))
    def randpad(n):                                                 #rand padding
        return ''.join(chr(randint(0,255)) for i in range(n))
    
    data = randpad(randint(5,10)) + data + randpad(randint(5,10))
    data  = exp1(data)
    key = randkey()
    flag = randint(0,1)
    if(flag):
        return cbc(data, key, randpad(16))
    else:
        return aes_ecb(data,key)
def detect(s):
    sto = []
    for i in range(0,len(s),16):
        a = s[i,i+16]
        if a in sto:
            return True    #ecb
        sto.append(a)
    return False    #cbc

def exp4():
    def exp1(block):
        padding_len = 16 -  (len(block)%16)
        #print chr(19)
        return block + chr(padding_len) * padding_len
    def randpad(n):                                                 #rand padding
        return ''.join(chr(randint(0,255)) for i in range(n))
    def randkey():                                                  #rand key
        return ''.join(chr(randint(0,255)) for i in range(16))
    key = randkey()
    def aes_ecb(data,key):                #AES ecb
        cipher = AES.new(key, AES.MODE_ECB)
        return cipher.encrypt(data)
    def oracle(S):
        data = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A / IE5vLCBJIGp1c3QgZHJvdmUgYnkK"
        return aes_ecb(exp1(S + b64decode(data)),key)
    def oracle2(S):
        data = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A / IE5vLCBJIGp1c3QgZHJvdmUgYnkK"
        return aes_ecb(exp1(randpad(8)+S + b64decode(data)),key)
            #模拟8个rand
    def  crack():
        get = ''
        '''
        第一次在前面填充15个A，配和爆破。爆破出第一个block的最后一位也就是明文的第一位
        第二次填充14个A 。爆破明文第二位
        '''
        for i in range(16,0,-1):
            padding = 'A'*(i-1)    #第一轮15个A
            enc_padding = oracle(padding)[0:16]
            print padding+get
            for s in range(256):
                test = padding +get+chr(s)
                test_enc  = oracle(test)[0:16]
                if enc_padding == test_enc:
                    get+=chr(s)
                    break
    def prefix_crack():
        '''
        prefix = 0
        for i in range(32,48):
            padding = 'A'*i
            enc = oracle(padding)
            '''
        get = ''
        for i in range(16-8,0,-1):
            padding = 'A'*(i-1)    #第一轮15个A
            enc_padding = oracle2(padding)[0:16]
            print padding+get
            for s in range(256):
                test = padding +get+chr(s)
                test_enc  = oracle2(test)[0:16]
                if enc_padding == test_enc:
                    get+=chr(s)
                    break
    prefix_crack()
def exp5():
    def xor_str(x, y):
        return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(x, y))
    def randpad(n):                                                 #rand padding
        return ''.join(chr(randint(0,255)) for i in range(n))
    def aes_ecb(data,key):                #AES ecb
        cipher = AES.new(key, AES.MODE_ECB)
        return cipher.encrypt(data)
    def cbc(data,key,iv):
        result = ''
        old = iv
        for i in range(0,len(data),16):
            new  = data[i:i+16]
            old = aes_ecb(xor_str(old,new), key)
            result += old
        return result

    key = randpad(16)
    iv = randpad(16)
    def fix(data):
        data = data.replace(';', '').replace('=', '')
        data = "comment1=cooking%20MCs;userdata=" + data
        data = data + ";comment2=%20like%20a%20pound%20of%20bacon"
        print "原始明文：%s\n"%(data)
        return cbc(exp1(data), key, iv)
    old =  fix('A'*16)
    chunk = old[16:32]   #%20MCs;userdata=
    hack = xor_str(chunk,xor_str("AA;admin=true;AA","A"*16))
    new = old.replace(chunk,hack)  ##modify
    aes = AES.new(key,AES.MODE_CBC,iv)
    print "修改后的明文：%s\n"%(aes.decrypt(new))
exp5()
'''
for i in reversed(range(0,8)):
    print i 
    '''
    
