import tqdm
from Crypto.Cipher import AES
from Crypto.Util import Counter
import os

def decrypt(msg, key):
    cipher = AES.new(key, AES.MODE_CTR, counter=Counter.new(128)) # I was told, CTR can't be broken!
    plaintext = cipher.decrypt(msg)
    return plaintext.decode()

msg = b'This is just a test message and can totally be ignored.' # Just checking functionality

with open('msg.txt', 'r') as f:
    encryptedmsg = bytes.fromhex(f.readline().strip())
    encryptedflag = bytes.fromhex(f.readline().strip())

print(encryptedmsg)
print(encryptedflag)

key = bytes([b1 ^ b2 for b1, b2 in zip(encryptedmsg, msg)])
print(decrypt(encryptedmsg, key))

