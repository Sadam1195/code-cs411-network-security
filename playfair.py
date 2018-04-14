def gen_matrix(key):
    m = list(key.upper())
    for ch_int in range(ord('A'), ord('Z')+1):
        ch = chr(ch_int)
        if ch == "J": continue
        if not ch in m: m.append(ch)
    return [m[i:i+5] for i in range(0, 25, 5)]

def find(matrix, ch):
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if ch == matrix[x][y]:
                return (x, y)
    return (-1, -1)

def playfair_encrypt(plain_text, key):
    plain_text = plain_text.upper().replace("J", "I")
    matrix = gen_matrix(key)
    print matrix
    encrypted_text = ""
    for i in range(0, len(plain_text) - 1, 2):
        first_ch = plain_text[i] 
        second_ch = plain_text[i+1]

        x0, y0 = find(matrix, first_ch)
        x1, y1 = find(matrix, second_ch)
        if x0 == x1: # Same row
            _x0, _y0 = x0, (y0+1)%5
            _x1, _y1 = x1, (y1+1)%5
        elif y0 == y1: # Same col
            _x0, _y0 = (x0+1)%5, y0
            _x1, _y1 = (x1+1)%5, y1
        else:
            _x0, _y0 = x0, y1
            _x1, _y1 = x1, y0
        encrypted_text += matrix[_x0][_y0] + matrix[_x1][_y1]
    return encrypted_text

def playfair_decrypt(encrypted_text, key):
    encrypted_text = encrypted_text.upper().replace("J", "I")
    matrix = gen_matrix(key)
    print matrix
    plain_text = ""
    for i in range(0, len(encrypted_text) - 1, 2):
        first_ch = encrypted_text[i] 
        second_ch = encrypted_text[i+1]

        x0, y0 = find(matrix, first_ch)
        x1, y1 = find(matrix, second_ch)
        if x0 == x1: # Same row
            _x0, _y0 = x0, (y0-1)%5
            _x1, _y1 = x1, (y1-1)%5
        elif y0 == y1: # Same col
            _x0, _y0 = (x0-1)%5, y0
            _x1, _y1 = (x1-1)%5, y1
        else:
            _x0, _y0 = x0, y1
            _x1, _y1 = x1, y0
        plain_text += matrix[_x0][_y0] + matrix[_x1][_y1]
    return plain_text

plain_text = "SYEDOWAISALICH" # Must be event
encrypted_text = playfair_encrypt(plain_text, "MONARCHY")
decrypted_text = playfair_decrypt(encrypted_text, "MONARCHY")
print ("plain_text:\t{} \nencrypted_text:\t{} \ndecrypted_text:\t{}\n").format(plain_text, encrypted_text, decrypted_text)