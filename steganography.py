from scipy import misc
import numpy as np
import math

def str2bin(s):
	return "".join([bin(ord(c))[2:].zfill(8) for c in s])

def bin2str(b):
	return "".join([chr(int(b[i:i+8], 2)) for i in range(0, len(b), 8)])

def steg_encode(image_in, msg, image_out=None):
	msg += "\0"
	msg_binary = str2bin(msg)
	msg = bin2str(msg_binary)

	image = misc.imread(image_in)
	height, width, channels = image.shape
	msg_binary_count = len(msg_binary)
	msg_binary_idx = 0
	max_char_allowed = (height * width * channels)
	
	print "> INFO: Message Size: " + str(msg_binary_count / 8) + " characters"
	print "> INFO: Max Size Allowed: " + str(max_char_allowed / 8) + " characters"

	if msg_binary_count > max_char_allowed:
		raise Exception("Message to large.")

	for i in range(height):
		for j in range(width):
			for c in range(channels):
				if msg_binary[msg_binary_idx] == "0":
					image[i][j][c] &= 0xFE # 8bit number 	
				else:
					image[i][j][c] |= 0x01 # 8bit number 

				msg_binary_idx += 1
				if msg_binary_idx == msg_binary_count: break
			if msg_binary_idx == msg_binary_count: break
		if msg_binary_idx == msg_binary_count: break

	if image_out:
		misc.imsave(image_out, image)
	else:
		return image
			
def steg_decode(image):
	if type(image) is not np.ndarray:
		image = misc.imread(image) # if path then read file
	height, width, channels = image.shape
	out_msg = ""
	for i in range(height):
		for j in range(width):
			for c in range(channels):
				if image[i][j][c] & 1 == 1:
					out_msg += "1"
				else:
					out_msg += "0"
				if out_msg[-8:] == "00000000": break
			if out_msg[-8:] == "00000000": break
		if out_msg[-8:] == "00000000": break

	return bin2str(out_msg[:-8])

# Maintain image as numpy array
msg = "Steganography using NumPy. Owais, Bilal, Ali"
encoded_image = steg_encode("in.png", msg) # set third parameter to save image eg. "out.jpg"
encoded_message = steg_decode(encoded_image)
print "Message: " + msg
print "Encoded Message: " + encoded_message
print

# Saving and loading image from file
msg = "Steganography using file. Owais, Bilal, Ali"
steg_encode("in.png", msg, "out.png") # set third parameter to save image eg. "out.jpg"
encoded_message = steg_decode("out.png")
print "Message: " + msg
print "Encoded Message: " + encoded_message