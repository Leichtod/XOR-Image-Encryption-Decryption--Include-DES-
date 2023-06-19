# XOR-DES Decryption

from PIL import Image
from Crypto.Cipher import DES

MODES = ["RGB", "RGBA"]


def xor(pixel, mode, key):
    red = int(pixel[0]) ^ int(key[0])
    green = int(pixel[1]) ^ int(key[1])
    blue = int(pixel[2]) ^ int(key[2])

    if mode == "RGBA":  # Need Alpha if RGBA
        return red, green, blue, 255
    else:
        return red, green, blue


with open("file_paths/decrypt.txt", "r") as f:
    dP = f.read()
    decryptPaths = dP.split("\n")

image = Image.open(f"{decryptPaths[0]}")

pix = image.load()
width, height = image.size

mainKey = []
mainKey2 = []
aLength = 0

# DES DECRYPT-1
with open(f"{decryptPaths[1]}", "rb") as f:
    desKey = f.read()

if len(desKey) > 8:
    desKey = desKey[:8]

cipher3 = DES.new(desKey, DES.MODE_OFB)
with open(f"{decryptPaths[2]}", "rb") as f:
    msg = f.read()
iv = msg[:8]
cipher3 = DES.new(desKey, DES.MODE_OFB, iv=iv)
decrypted_msg = cipher3.decrypt(msg[8:])
mainKey = decrypted_msg.decode("utf-8").split("\n")

# DES DECRYPT-2
with open(f"{decryptPaths[3]}", "rb") as f:
    desKey2 = f.read()

cipher4 = DES.new(desKey2, DES.MODE_OFB)
with open(f"{decryptPaths[4]}", "rb") as f:
    msg2 = f.read()
iv2 = msg2[:8]
cipher4 = DES.new(desKey2, DES.MODE_OFB, iv=iv2)
decrypted_msg2 = cipher4.decrypt(msg2[8:])
mainKey2 = decrypted_msg2.decode("utf-8").split("\n")

aLength = len(mainKey)
aCount = 0
for x in range(0, width):
    for y in range(0, height):
        if aCount >= aLength:
            aCount = 0
        pix[x, y] = xor((mainKey2[aCount], mainKey2[aCount + 1], mainKey2[aCount + 2]), image.mode,
                        (mainKey[aCount], mainKey[aCount + 1], mainKey[aCount + 2]))
        aCount += 3  # RED - GREEN - BLUE = 252, 235, 636

srIndex2 = decryptPaths[0].find(".")
srFormat2 = decryptPaths[0][srIndex2 + 1:]
image.save(f"{decryptPaths[5]}/decryptedImage.{srFormat2}")
