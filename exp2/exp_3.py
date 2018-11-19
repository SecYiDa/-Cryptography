from operator import methodcaller
import re
import numpy
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto import Random

def main():
	blockSize = 16 	
	def cbcDecrypt(key, cypherText, blockSize):
		k = key.decode('hex')
		ct = cypherText.decode('hex')
		IV = ct[:blockSize]
		ct1 = ct[blockSize:]
		aes = AES.new(k,AES.MODE_CBC,IV)
		decrypted_text = aes.decrypt(ct1)
		return decrypted_text
	def ctrDecrypt(key, cypherText, blockSize):
		k = key.decode('hex')
		ct = cypherText.decode('hex')
		iv = ct[:blockSize]
		ct1 = ct[blockSize:]
		ctr = Counter.new(128,initial_value=long(iv.encode('hex'),16))       #4-bytes
		obj = AES.new(k,AES.MODE_CTR,counter=ctr)
		decrypted_text = obj.decrypt(ct1)
		return decrypted_text

	p1 = cbcDecrypt("140b41b22a29beb4061bda66b6747e14", "4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81", blockSize)	
	p2 = cbcDecrypt("140b41b22a29beb4061bda66b6747e14", "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253", blockSize)	
	p3 = ctrDecrypt("36f18357be4dbd77f050515c73fcf9f2", "69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329", blockSize)	
	p4 = ctrDecrypt("36f18357be4dbd77f050515c73fcf9f2", "770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451", blockSize)	

	print p1
	print p2
	print p3
	print p4
main()