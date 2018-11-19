# -*- coding: utf-8 -*-
from __future__ import division 
import logging  # 引入logging模块
logging.basicConfig(level=logging.NOTSET)
import base64
import re
from string import ascii_lowercase
from binascii import b2a_hex, a2b_hex
from bb import ming

def q1(para):
    a = base64.b64encode(para)
    print('\033[1;31;40m')
    print "第一题："
    print "base64 =" + a
    print('\033[0m')

def q2(s1, s2):    
    s1 = s1.decode('hex') 
    s2 = s2.decode('hex')
    print('\033[1;32;40m')
    print "第二题："
    print ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))
    print('\033[0m')

def q3(s1,s2):
    s1 = s1.decode('hex')
    ans = ''
    for i in s1:

        ans += chr(ord(i) ^ ord(s2))
    print "尝试[%c] %s" % (s2, ans)
    print ans     #Cooking MC's like a pound of bacon
def q4(s2):
    def get_english_score(input_bytes):

        character_frequencies = {'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,'m': .02406, 'n': .06749, 'o': .07507, 'p': .01929,'q': .00095, 'r': .05987, 's': .06327, 't': .09056,'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,'y': .01974, 'z': .00074, ' ': .13000}
        return sum([character_frequencies.get(byte,0) for byte in input_bytes.lower()])    #get(xx,0)找不到时候返回0


    score = [] 
    txt = open('4.txt')
    tt = []
    for line in txt:
        tt.append(line)
    line =tt[170][0:60]
    line  =line.decode('hex')
    ans = ''
    for i in line:
        ans += chr(ord(i) ^ s2)
    print "尝试[%d] %s" % (s2, ans)
def q5(s1,key):
    length = len(key)
    ans = ''
    for i in range(len(s1)):
        ans+= str(hex(ord(s1[i]) ^ ord(key[i%length]))).replace('0x','')
    print ans

aa = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
q1(aa)
aa= '1c0111001f010100061a024b53535009181c'
bb='686974207468652062756c6c277320657965'
q2(aa,bb)
print('\033[1;36;40m')
print "第三题："    
d = 'ABCDEFGHIJKLMNOPQRSTUVWX'
aa = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
for i in d:
    q3(aa,i)
print('\033[0m')
print('\033[1;33;40m')
print "第四题："
d = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
for i in xrange(54):
    q4(i)
print('\033[0m')

e = "Burning 'em, if you ain't quick and nimble"
print('\033[1;34;40m')
print "第五题："
q5(e,'ICE')
print('\033[0m')


def q6():
    def single_char_xor(input_bytes, char_value):
        output_bytes = ''
        for byte in input_bytes:
            output_bytes += chr(ord(byte) ^ char_value)   #异或结果添加到字符串中
        return output_bytes
    def get_english_score(input_bytes):
        character_frequencies = {
            'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
            'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
            'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
            'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
            'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
            'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
            'y': .01974, 'z': .00074, ' ': .13000
        }
        return sum([character_frequencies.get(byte, 0) for byte in input_bytes.lower()])    # 如果没有获取到这个字符的frequency就用0作为值
    def bruteforce_single_char_xor(ciphertext):
        potential_messages = []
        for key_value in range(0,255):
            message = single_char_xor(ciphertext, key_value)
            score = get_english_score(message)
            data = {
                'message': message,
                'score': score,
                'key': key_value
                }
            potential_messages.append(data)

        return sorted(potential_messages, key=lambda x: x['score'], reverse=True)[0]
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    def strxorr(a, b):  
            if len(a) > len(b):
                return "".join([chr(x ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
            else:
                return "".join([chr(x ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])
    def strxor(a, b):   
            if len(a) > len(b):
                return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
            else:
                return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])
    def crack(cypherTexts):
        key = 0
        max_pos =0
        for a in cypherTexts:
            possible_spaces = 0
            for b in cypherTexts:
                if a == b: continue
                c = strxor(a, b)
                if c not in letters and c != 0: continue
                possible_spaces += 1 
            if possible_spaces >= max_pos:   
                key = ord(a) ^ 0x20
        return key
    
        '''
           #if key == 84:
                logging.warning(possible_spaces)
                logging.warning(key)
                print '\n'
                #raw_input()
        '''
    '''解码base64
    '''
    text = open('6.txt')
    encode = text.read()

    encode = base64.b64decode(encode)	
    print ord(encode[0])


    '''
        以29个位置拆分block
    '''
    block = [[] for _ in range(29)]
    for i in range(len(encode)):
        block[i % 29].append(encode[i])

    '''
        对29个位置，每个位置进行这种空格法
    '''
    key = ''
    for i in block:
        key +=  chr(crack(i))
    print key





    key = []
    for i in block:
        key.append(chr(crack(i)))
    print key



    key = []
    for i in block:
        key.append(bruteforce_single_char_xor(i)['key'])
    keys = ''
    for i in key:
        keys+=chr(i)
    print('\033[1;35;40m')
    print keys + '\n'
    result = ''
    for i in range(len(encode)):
        result += strxor(keys[i % 29],encode[i])
    print result
q6()







