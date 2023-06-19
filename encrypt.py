# XOR-DES Encryption

import random
import os
from PIL import Image
from Crypto.Cipher import DES

MODES = ["RGB", "RGBA"]


def xor(pixel, mode, key):
    red = pixel[0] ^ int(key[0])
    green = pixel[1] ^ int(key[1])
    blue = pixel[2] ^ int(key[2])

    if mode == "RGBA":
        return red, green, blue, 255
    else:
        return red, green, blue


with open("file_paths/encrypt.txt", "r") as f:
    s1 = f.read()
    encryptPaths = s1.split("\n")

image = Image.open(f"{encryptPaths[0]}")
if image.mode == "RGBA":
    image = image.convert("RGB")
pix = image.load()
width, height = image.size

# KEY
randKey = []
for x in range(0, width * height * 3):
    randKey.append(random.SystemRandom().randint(0, 255))

mainKey = []
aLength = len(randKey)
for i in range(0, aLength):
    mainKey.append(str(randKey[i]))

# DES ENCRYPT
desKey = os.urandom(8)
with open(f"{encryptPaths[1]}/des.txt", "wb") as f00:
    f00.write(desKey)

cipher = DES.new(desKey, DES.MODE_OFB)
joined_list = "\n".join(mainKey)
plaintext = joined_list.encode("utf8")
msg = cipher.iv + cipher.encrypt(plaintext)
with open(f"{encryptPaths[2]}/key.txt", "wb") as f:
    f.write(msg)

aCount = 0
aLength2 = len(mainKey)

mainKey2 = []
for x in range(0, width):
    for y in range(0, height):
        if aCount >= aLength2:
            aCount = 0
        pix[x, y] = xor(pix[x, y], image.mode, (mainKey[aCount], mainKey[aCount + 1], mainKey[aCount + 2]))
        sideKey = list(pix[x, y])
        for i in range(0, len(sideKey)):
            mainKey2.append(str(sideKey[i]))
        aCount += 3

# DES ENCRYPT 2
desKey2 = os.urandom(8)
with open(f"{encryptPaths[3]}/des2.txt", "wb") as f0:
    f0.write(desKey2)

cipher2 = DES.new(desKey2, DES.MODE_OFB)
joined_list2 = "\n".join(mainKey2)
plaintext2 = joined_list2.encode("utf8")
msg2 = cipher2.iv + cipher2.encrypt(plaintext2)
with open(f"{encryptPaths[4]}/key2.txt", "wb") as f2:
    f2.write(msg2)

image.save(f"{encryptPaths[5]}/encryptedImage.jpg")
