# Author: soachishti (p146011@nu.edu.pk)
# Link: http://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm

from bitarray import bitarray


class DES():

    pc_1 = [
        57, 49,    41,   33,    25,    17,    9,
        1,  58,    50,   42,    34,    26,   18,
        10,  2,    59,   51,    43,    35,   27,
        19, 11,     3,   60,    52,    44,   36,
        63, 55,    47,   39,    31,    23,   15,
        7,   2,    54,   46,    38,    30,   22,
        14,  6,    61,   53,    45,    37,   29,
        21, 13,     5,   28,    20,    12,    4
    ]

    pc_2 = [
        14,    17,   11,    24,     1,    5,
        3,  28, 15,  6, 21, 10,
        23,   19,  12,   4,  26, 8,
        16,    7,  27,  20,  13, 2,
        41,   52,  31,  37,  47, 55,
        30,   40,  51,  45,  33, 48,
        44,   49,  39,  56,   34,  53,
        46,   42,  50,  36,  29, 32
    ]

    ip = [
        58,    50,   42,    34,    26,   18,    10,    2,
        60,    52,   44,    36,    28,   20,    12,    4,
        62,    54,   46,    38,    30,   22,    14,    6,
        64,    56,   48,    40,    32,   24,    16,    8,
        57,    49,   41,    33,    25,   17,     9,    1,
        59,    51,   43,    35,    27,   19,    11,    3,
        61,    53,   45,    37,    29,   21,    13,    5,
        63,    55,   47,    39,    31,   23,    15,    7
    ]

    e_selection = (
        32,     1,    2,     3,     4,    5,
        4,     5,    6,     7,     8,    9,
        8,     9,   10,    11,    12,   13,
        12,    13,   14,    15,    16,   17,
        16,    17,   18,    19,    20,   21,
        20,    21,   22,    23,    24,   25,
        24,    25,   26,    27,    28,   29,
        28,    29,   30,    31,    32,    1,
    )

    s_box = [
        [
            (14,  4,  13,  1,   2, 15,  11,  8,
              3, 10,   6, 12,   5,  9,   0,  7),
            (0, 15,   7,  4,  14,  2,  13,  1,
            10,  6,  12, 11,   9,  5,   3,  8),
            (4,  1,  14,  8,  13,  6,   2, 11,
            15, 12,   9,  7,   3, 10,   5,  0),
            (15, 12,   8,  2,   4,  9,   1,  7,
             5, 11,   3, 14,  10,  0,   6, 13),
        ], [
            (15,  1,   8, 14,   6, 11,   3,  4,
             9,  7,   2, 13,  12,  0,   5, 10,),
            (3, 13,   4,  7,  15,  2,   8, 14,
             12,  0,   1, 10,   6,  9,  11,  5,),
            (0, 14,   7, 11,  10,  4,  13, 1,
             5,  8,  12,  6,   9,  3,   2, 15,),
            (13,  8,  10,  1,   3, 15,   4,  2,
             11,  6,   7, 12,   0,  5,  14,  9,),
        ], [
            (10,  0,   9, 14,   6,  3,  15,  5,
             1, 13,  12,  7,  11,  4,   2,  8,),
            (13,  7,   0,  9,   3,  4,   6, 10,
             2,  8,   5, 14,  12, 11,  15,  1,),
            (13,  6,   4,  9,   8, 15,   3,  0,
             11,  1,   2, 12,   5, 10,  14,  7,),
            (1, 10,  13,  0,   6,  9,   8,  7,
             4, 15,  14,  3,  11,  5,   2, 12,),
        ], [
            (7, 13,  14,  3,   0,  6,   9, 10,
             1,  2,   8,  5,  11, 12,   4, 15,),
            (13,  8,  11,  5,   6, 15,   0,  3,
             4,  7,   2, 12,   1, 10,  14,  9,),
            (10,  6,   9,  0,  12, 11,   7, 13,
             15,  1,   3, 14,   5,  2,   8,  4,),
            (3, 15,   0,  6,  10,  1,  13,  8,
             9,  4,   5, 11,  12,  7,   2, 14,),
        ], [
            (2, 12,   4,  1,   7, 10,  11,  6,
             8,  5,   3, 15,  13,  0,  14,  9,),
            (14, 11,   2, 12,   4,  7,  13,  1,
             5,  0,  15, 10,   3,  9,   8,  6,),
            (4,  2,   1, 11,  10, 13,   7,  8,
             15,  9,  12,  5,   6,  3,   0, 14,),
            (11,  8,  12,  7,   1, 14,   2, 13,
             6, 15,   0,  9,  10,  4,   5,  3,),
        ], [
            (12,  1,  10, 15,   9,  2,   6,  8,
             0, 13,   3,  4,  14,  7,   5, 11,),
            (10, 15,   4,  2,   7, 12,   9,  5,
             6,  1,  13, 14,   0, 11,   3,  8,),
            (9, 14,  15,  5,   2,  8,  12,  3,
             7,  0,   4, 10,   1, 13,  11,  6,),
            (4,  3,   2, 12,   9,  5,  15, 10,
             11, 14,   1,  7,   6,  0,   8, 13,),
        ], [
            (4, 11,   2, 14,  15,  0,   8, 13,   3, 12,  9,  7,   5, 10,   6,  1,),
            (13,  0,  11,  7,   4,  9,   1, 10,
             14,  3,  5, 12,   2, 15,   8,  6,),
            (1,  4,  11, 13,  12,  3,   7, 14,  10, 15,  6,  8,   0,  5,   9,  2,),
            (6, 11,  13,  8,   1,  4,  10,  7,   9,  5,  0, 15,  14,  2,   3, 12,),
        ], [
            (13,  2,   8,  4,   6, 15,  11,  1,
             10,  9,   3, 14,   5,  0,  12,  7,),
            (1, 15,  13,  8,  10,  3,   7,  4,
             12,  5,   6, 11,   0, 14,   9,  2,),
            (7, 11,   4,  1,   9, 12,  14,  2,
             0,  6,  10, 13,  15,  3,   5,  8,),
            (2,  1,  14,  7,   4, 10,   8, 13,  15, 12,   9,  0,   3,  5,   6, 11,)
        ]
    ]

    hex2bin = {
        "0": (0, 0, 0, 0), "1": (0, 0, 0, 1), "2": (0, 0, 1, 0),
        "3": (0, 0, 1, 1), "4": (0, 1, 0, 0), "5": (0, 1, 0, 1),
        "6": (0, 1, 1, 0), "7": (0, 1, 1, 1), "8": (1, 0, 0, 0),
        "9": (1, 0, 0, 1), "a": (1, 0, 1, 0), "b": (1, 0, 1, 1),
        "c": (1, 1, 0, 0), "d": (1, 1, 0, 1), "e": (1, 1, 1, 0),
        "f": (1, 1, 1, 1)
    }

    int2bin = [
        (0, 0, 0, 0),  # 0
        (0, 0, 0, 1),  # 1
        (0, 0, 1, 0),  # 2
        (0, 0, 1, 1),  # 3
        (0, 1, 0, 0),  # 4
        (0, 1, 0, 1),  # 5
        (0, 1, 1, 0),  # 6
        (0, 1, 1, 1),  # 7
        (1, 0, 0, 0),  # 8
        (1, 0, 0, 1),  # 9
        (1, 0, 1, 0),  # 10
        (1, 0, 1, 1),  # 11
        (1, 1, 0, 0),  # 12
        (1, 1, 0, 1),  # 13
        (1, 1, 1, 0),  # 14
        (1, 1, 1, 1),  # 15
    ]

    p = [
        16,   7,  20,  21,
        29,  12,  28,  17,
        1, 15, 23,  26,
        5, 18, 31,  10,
        2,  8, 24,  14,
        32,  27,   3,   9,
        19,  13,  30,   6,
        22,  11,   4,  25,
    ]

    ip_inverse = [
        40,     8,   48,    16,    56,   24,    64,   32,
        39,     7,   47,    15,    55,   23,    63,   31,
        38,     6,   46,    14,    54,   22,    62,   30,
        37,     5,   45,    13,    53,   21,    61,   29,
        36,     4,   44,    12,    52,   20,    60,   28,
        35,     3,   43,    11,    51,   19,    59,   27,
        34,     2,   42,    10,    50,   18,    58,   26,
        33,     1,   41,     9,    49,   17,    57,   25,
    ]

    iterations = 16
    key_shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    def __init__(self):
        self.keys = []

    def _hexstr2bitarray(self, message):
        message = message.lower()
        hex2bin = {
            "0": (0, 0, 0, 0), "1": (0, 0, 0, 1), "2": (0, 0, 1, 0),
            "3": (0, 0, 1, 1), "4": (0, 1, 0, 0), "5": (0, 1, 0, 1),
            "6": (0, 1, 1, 0), "7": (0, 1, 1, 1), "8": (1, 0, 0, 0),
            "9": (1, 0, 0, 1), "a": (1, 0, 1, 0), "b": (1, 0, 1, 1),
            "c": (1, 1, 0, 0), "d": (1, 1, 0, 1), "e": (1, 1, 1, 0),
            "f": (1, 1, 1, 1)
        }
        l = []
        for m in message:
            l.extend(hex2bin[m])
        return bitarray(l)

    def _apply(self, p, k):
        new_k = bitarray()
        for idx in p:
            new_k.append(k[idx-1])
        return new_k

    def _leftrotate(self, ba, count):
        return ba[count:] + ba[:count]

    def _f(self, r, k):
        e_r = self._apply(self.e_selection, r)
        k_e_r = k ^ e_r
        ret = bitarray()
        bits_box_size = 6
        for s_idx in range(0, 8):
            # our 6 bits
            b = k_e_r[s_idx*bits_box_size: (s_idx*bits_box_size)+bits_box_size]

            i = bitarray([b[0], b[-1]])  # get first and last bit
            i = int(i.to01(), 2)  # convert it to int

            j = b[1: -1]  # get center 4 bits
            j = int(j.to01(), 2)  # convert it to int

            s_val = self.s_box[s_idx][i][j]
            ret.extend(self.int2bin[s_val])
        return self._apply(self.p, ret)

    def process_key(self, key):
        k = self._hexstr2bitarray(key)
        k_plus = self._apply(self.pc_1, k)

        c = k_plus[0:28]
        d = k_plus[28:]

        key = c+d
        key = self._apply(self.pc_2, key)
        self.keys = [key]

        #print "c0:", c
        #print "c1:", d
        #print "key:", keys[0]
        # print

        for i in range(1, self.iterations+1):
            c = self._leftrotate(c, self.key_shifts[i-1])
            d = self._leftrotate(d, self.key_shifts[i-1])

            key = c+d
            key = self._apply(self.pc_2, key)
            self.keys.append(key)

            #print "c{}: {}".format(i, c)
            #print "d{}: {}".format(i, d)
            #print "key{}: {}".format(i, keys[i])
            # print

    def process_message(self, m):
        m += "\r\n"
        divisor = 16
        hex_message = m.encode('hex')
        if len(m) % divisor != 0:
            size = len(m)
            pad = divisor - (size % divisor)
            hex_message = hex_message.ljust(size+pad, '0')
        return hex_message

    def encrypt(self, hex_message, key):
        self.process_key(key)
        m = self._hexstr2bitarray(hex_message)
        m_ip = self._apply(self.ip, m)  # _apply initial IP
        l = m_ip[:32]
        r = m_ip[32:]

        for i in range(1, self.iterations+1):
            l, r = r, l ^ self._f(r, self.keys[i])

        c = r + l
        c = self._apply(self.ip_inverse, c)
        c_bin = c.to01()

        return "{0:0>4X}".format(int(c_bin, 2)).lower()

    def decrypt(self, message, key):
        self.process_key(key)  # generate 16 keys
        m = self._hexstr2bitarray(message)
        m_ip = self._apply(self.ip, m)  # _apply initial IP
        l = m_ip[:32]
        r = m_ip[32:]

        for i in range(self.iterations, 0, -1):
            l, r = r, l ^ self._f(r, self.keys[i])

        c = r + l
        c = self._apply(self.ip_inverse, c)
        return c.tobytes().encode('hex')
