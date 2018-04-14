# Author: soachishti (p146011@nu.edu.pk)
# Link: http://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm

from des import DES

d = DES()

print "\n" + "="*5 + "HEX Demo" + "="*5 + "\n"

hex_message = "0123456789abcdef"
key = "133457799BBCDFF1" # Must be hex
encryted = d.encrypt(hex_message, key)
decrypted = d.decrypt(encryted, key)

print "Message: ", hex_message
print "Key: ", key
print "Encryted: ", encryted
print "Decrypted: ", decrypted

print "\n" + "="*5 + "ASCII Demo" + "="*5 + "\n"

ascii_message = "OwaisAli"
hex_message = d.process_message(ascii_message)
encryted = d.encrypt(hex_message, key)
decrypted = d.decrypt(encryted, key)

print "ASCII Message: ", ascii_message
print "Hex Message: ", hex_message
print "Key: ", key
print "Encryted: ", encryted
print "Decrypted: ", decrypted.decode('hex').split('\0')[0]