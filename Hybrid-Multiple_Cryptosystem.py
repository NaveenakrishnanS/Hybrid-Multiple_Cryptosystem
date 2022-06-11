import secrets
from Crypto.Cipher import AES
import rsa
def keys():
    global aeskey, publickey, privatekey
    #key generation
    aeskey = secrets.token_bytes(32)
    print("\nAES PUBLIC KEY: ",aeskey)
    publickey, privatekey = rsa.newkeys(1024)
    print("\nRSA PUBLIC KEY: ",publickey)
    print("\nRSA PRIVATE KEY: ",privatekey)
    
#input
message=input("\nenter the message: ")
keys()
def encrypt():
    global nonce,enc,cipherkey
    #aes encryption
    cipherAESe=AES.new(aeskey,AES.MODE_GCM)
    nonce=cipherAESe.nonce
    ciphertext=cipherAESe.encrypt(message.encode("utf-8"))
    print("\n AES ciphertext:",ciphertext)
    #rsa encryption
    enc= rsa.encrypt(ciphertext,publickey)
    print("\n encrypted text by rsa:", enc)
    #encrypting aes key
    cipherkey=rsa.encrypt(aeskey,publickey)
    print("\n Encrypted AES KEY: ",cipherkey)
def decrypt():
    #decrypting aes key
    dicipheredkey =rsa.decrypt(cipherkey,privatekey)
    print("\n Decrypted AES KEY: ",dicipheredkey)
    #rsa decryption
    dec= rsa.decrypt(enc, privatekey)
    print("\n decrypted by rsa:", dec)
    #aes decryption
    cipherAESd=AES.new(dicipheredkey,AES.MODE_GCM,nonce=nonce)
    decrypted=cipherAESd.decrypt(dec).decode("utf-8")
    print("\ndecrypted message by aes:",decrypted)
encrypt()
decrypt()
