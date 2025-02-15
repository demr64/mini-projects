import sys

CHUNK_SIZE = 512
WORD_SIZE = 32

def leftrotate(msg, n):
    x = msg[:n]
    y = msg[n:]
    return y + x
  
def breaknchunks(msg, size):
    chunks = []
    binary_length = int(len(msg)/size)
    for i in range(0, binary_length):
        chunks.append(msg[(i*size):(i+1)*size])
    return chunks


def sha1(msg_txt):
    # data preprocessing
    # starting variables for the core algorithm
    h0 = int('67452301', 16)
    h1 = int('EFCDAB89', 16)
    h2 = int('98BADCFE', 16)
    h3 = int('10325476', 16)
    h4 = int('C3D2E1F0', 16)
  
    msg_arr = [ord(i) for i in msg_txt]
    msg_bits = [(format(i, '08b')) for i in msg_arr] 
    msg_len = len(msg_bits)*8
    msg_bit_repr = ""
    
    for i in msg_bits:
        msg_bit_repr += i
    msg_bit_repr += '1'
    
    for k in range(0, CHUNK_SIZE):
        if(len(msg_bit_repr)%CHUNK_SIZE != 448):
            msg_bit_repr += '0'
            continue
        break
    
    msg_bit_repr += format(msg_len, '064b')

    # core algorithm
    chunks = breaknchunks(msg_bit_repr, CHUNK_SIZE)
    for chunk in chunks:
        words = breaknchunks(chunk, WORD_SIZE)
        for i in range(16, 79+1):
            word_a = int(words[i-3], 2)
            word_b = int(words[i-8], 2)
            word_c = int(words[i-14], 2)
            word_d = int(words[i-16], 2)
            new_word = (word_a ^ word_b ^ word_c ^ word_d)
            
            new_word = format(new_word,'032b')
            new_word = leftrotate(new_word, 1) 
            words.append(new_word)

        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        for i in range(0, 79+1):
            if i >= 0 and i <= 19:
                # notice the and with the 0x value, lines like these
                # ensure that we keep working in 2^32.
                # this procedure will be done anytime we encounter an operation
                # that could cause an overflow.
                f = (b & c) | ((~b & 0xffffffff) & d)
                k = int('5A827999', 16)
            elif 20 <= i and i <= 39:
                f = b ^ c ^ d
                k = int('6ED9EBA1', 16)
            elif 40 <= i and i <= 59:
                f = (b & c) | (b & d) | (c & d) 
                k = int('8F1BBCDC', 16)
            elif 60 <= i and i <= 79:
                f = b ^ c ^ d
                k = int('CA62C1D6', 16)
        
            temp = int(leftrotate(format(a, '032b'), 5), 2) + f + e + k + int(words[i], 2) & 0xffffffff
            e = d
            d = c
            c = int(leftrotate(format(b, '032b'), 30), 2)
            b = a
            a = temp

        h0 = (h0+a) & 0xffffffff
        h1 = (h1+b) & 0xffffffff
        h2 = (h2+c) & 0xffffffff
        h3 = (h3+d) & 0xffffffff
        h4 = (h4+e) & 0xffffffff

    return hex((h0<<128) | (h1<<96) | (h2<<64) | (h3<<32) | (h4))

def main():
    msg = str(sys.argv[1])
    print("Hashed:", sha1(msg)[2:])

if __name__ == "__main__":
    main() 


