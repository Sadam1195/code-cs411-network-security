import numpy as np
from time import sleep
from math import ceil
from sympy.matrices import *

def tomatrix(s, x=2, y=2):
	return np.array([ord(ch)-65 for ch in s]).reshape(x, y)

def hillcipher_encrypt(msg, key, size = 2):
	k = tomatrix(key, size, size)
	m = tomatrix(msg, 1, -1)
	m = m.reshape(m.shape[1]/size, size, 1)
	e = ""
	for i in range(m.shape[0]):
		_e = np.dot(k, m[i]) % 26
		_e = _e.flatten()
		e += "".join([chr(val+65) for val in _e])
	return e

def hillcipher_decrypt(msg, key, size = 2):
	k = tomatrix(key, size, size)
	d = ceil(np.linalg.det(k)) % 26 # determinant
	mi = 1 # multiplicative_inverse
	while True:
		if ((d*mi) % 26) == 1:
			break
		mi += 1

	adjugate = np.array(Matrix(k).adjugate()) % 26 # Uses sympy

	km = (mi * adjugate) % 26 # keymatrix
	
	m = tomatrix(msg, 1, -1)
	m = m.reshape(m.shape[1]/size, size, 1)
	e = ""
	for i in range(m.shape[0]):
		_e = np.dot(km, m[i]) % 26
		_e = _e.flatten()
		e += "".join([chr(val+65) for val in _e])
	return e


# Size 2x2 
key = "hill".upper()
msg = "shortexample".upper() # must be divisible by size i.e. 2

encrypt = hillcipher_encrypt(msg, key, size=2)
decrypt = hillcipher_decrypt(encrypt, key, size=2)

print "Size: 2x2"
print "Message: ", msg
print "Encrypted: ", encrypt
print "Decrypted: ", decrypt
print "\n\n"

# Size 3x3 
key = "alphabeta".upper()
msg = "shortexample".upper() # must be divisible by size i.e. 3

encrypt = hillcipher_encrypt(msg, key, size=3)
decrypt = hillcipher_decrypt(encrypt, key, size=3)

print "Size: 3x3"
print "Message: ", msg
print "Encrypted: ", encrypt
print "Decrypted: ", decrypt