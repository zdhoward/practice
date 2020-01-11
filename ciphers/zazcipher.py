literals = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,.?/:;{[]}-=_+~!@#$%^&*()"
#obfuscated
literals = "tJ;EM mKrFzQ_SOT?]B[U@$yqec~fhd{=is&alxPIbnuRkC%Z(jDw#G:/)L,*.V!pov+HNYA^g-}WX"
key = 7

def shuffle(plaintext):
    shuffled = ""
    # shuffle plaintext
    for i in range(int(len(plaintext) / 3)):
         block = plaintext[i*3] + plaintext[i*3 + 1] + plaintext[i*3 + 2]
         old0 = block[0]
         old1 = block[1]
         old2 = block[2]
         block = old2 + old0 + old1
         shuffled += block
    shuffled += plaintext[len(plaintext) - (len(plaintext) % 3):len(plaintext)]
    return shuffled

def unshuffle(ciphertext):
    unshuffled = ""
    # unshuffle plaintext
    for i in range(int(len(ciphertext) / 3)):
         block = ciphertext[i*3] + ciphertext[i*3 + 1] + ciphertext[i*3 + 2]
         old0 = block[0]
         old1 = block[1]
         old2 = block[2]
         block = old1 + old2 + old0
         unshuffled += block
    unshuffled += ciphertext[len(ciphertext) - (len(ciphertext) % 3):len(ciphertext)]
    return unshuffled

def shift(plaintext):
    shifted = ""
    # Cipher shift
    tmp = []
    for i in range(len(plaintext)):
        pos = literals.find(plaintext[i])
        if pos >= 0:
            if pos + key > len(literals):
                pos = (pos + key) - len(literals)
            res = literals[pos + key]
        else:
            res = plaintext[i]
        tmp.append(res)
    # reconstruct ciphertext
    for i in range(len(tmp)):
        shifted += tmp[i]
    return shifted

def unshift(ciphertext):
    unshifted = ""

    tmp = []

    for i in range(len(ciphertext)):
        pos = literals.find(ciphertext[i])
        if pos >= 0:
            if pos - key < 0:
                pos = (pos - key) + len(literals)
            res = literals[pos - key]
        else:
            res = ciphertext[i]
        tmp.append(res)
    #reconstruct ciphertext
    for i in range(len(tmp)):
        unshifted += tmp[i]

    return unshifted

def encrypt(msg):
    msg = shuffle(msg)
    msg = shift(msg)
    return msg

def decrypt(msg):
    #msg = unshuffle(msg)
    msg = unshift(msg)
    msg = unshuffle(msg)
    return msg

def test():
    test = "This is my plaintext"
    test = "\nThis is a long paragraph with lots of exciting things\nI could go on and on about all of this stuff.\nLove, Zach!"
    test = "abcdefghijklmnopqrstuvwxyz-ABCDEFGHIJKLMNOPQRSTUVWXYZ_!@#$%^&*()"
    print ("Testing:   " + test)
    print ("Shuffle:   " + shuffle(test))
    print ("Shift:     " + shift(shuffle(test)))
    print ("Unshift:   " + unshift(shift(shuffle(test))))
    print ("Unshuffle: " + unshuffle(unshift(shift(shuffle(test)))))
    print ("")
    print ("Encrypt:   " + encrypt(test))
    print ("Decrypt:   " + decrypt(encrypt(test)))

if __name__ == "__main__":
    test()
