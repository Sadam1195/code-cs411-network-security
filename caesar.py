def caesar_encrypt(plain_text, jump):
    encrypted_text = ""
    for ch in plain_text:
        if ch.isalpha():
            base_val = ord('A') if ch.upper() == ch else ord('a')
            ch = (((ord(ch) - base_val) + jump) % 26) + base_val
            ch = chr(ch)
        encrypted_text += ch
    return encrypted_text

def caesar_decrypt(plain_text, jump):
    encrypted_text = ""
    for ch in plain_text:
        if ch.isalpha():
            base_val = ord('A') if ch.upper() == ch else ord('a')
            ch = (((ord(ch) - base_val) - jump) % 26) + base_val
            ch = chr(ch)
        encrypted_text += ch
    return encrypted_text


plain_text = "abcd efgh ijkl mnop qrst uvwx yz ABCD EFGH IJKL MNOP QRST UVWX YZ"

encrypted_text = caesar_encrypt(plain_text, 10)
decrypted_text = caesar_decrypt(encrypted_text, 10)

print ("plain_text:\t{} \nencrypted_text:\t{} \ndecrypted_text:\t{}\n").format(plain_text, encrypted_text, decrypted_text)