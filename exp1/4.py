# -*- coding: utf-8 -*-
from __future__ import division 
import re
import base64
import logging
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
def cut_text(text,lenth):    
    textArr = re.findall('.{'+str(lenth)+'}', text)  
    textArr.append(text[(len(textArr)*lenth):])    
    return textArr 
def crack(cypherTexts):
    key = 0
    max_pos = 0
    for a in cypherTexts:     #遍历组内所有字符，并将其与组内其他字符进行异或
        possible_spaces = 0
        for b in cypherTexts:
            if a == b: continue
            c = strxor(a, b)
            if c not in letters and c != 0: continue
            possible_spaces += 1
        if possible_spaces >= max_pos:  
            max_pos = possible_spaces
            key = ord(a) ^ 0x20
    return key



'''解码base64
'''
text = open('6.txt')
encode = text.read()
encode = base64.b64decode(encode)	


'''
    以29个位置拆分block
'''
block = [[] for _ in range(29)]
for i in range(len(encode)):
    block[i % 29].append(encode[i])

'''
    对29个位置，每个位置进行这种空格法
'''
#print crack(block[3])
#raw_input()
key = []
for i in block:
    key.append(crack(i))
print key
keys = ''
for i in key:
    keys+=chr(i)
print keys


raw_input()
