from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def encrypt(message):
    with open('key.pub', 'r') as f:
        key = f.read() 

    rsakey = RSA.importKey(key)
    rsakey = PKCS1_OAEP.new(rsakey)
    encrypted = rsakey.encrypt(message)
    return base64.b64encode(encrypted)

def decrypt(package):
    with open('key', 'r') as f:
        key = f.read() 

    rsakey = RSA.importKey(key) 
    rsakey = PKCS1_OAEP.new(rsakey)
    bytes = base64.b64decode(package)
    return rsakey.decrypt(bytes) 
