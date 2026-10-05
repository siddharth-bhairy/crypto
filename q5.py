from simplecrypt import encrypt, decrypt
import hashlib
import base64

text=input("enter the text : ")

key=input("enter encryption key : ")

print("\n1. Simple Crypt Encryption/Decryption")

encrypted=encrypt(key,text)
decrypted=decrypt(key,encrypted).decode()

print("encrypted text :",encrypted)
print("decrypted text :",decrypted)


print("\n2. Message Digest")

md5=hashlib.md5(text.encode()).hexdigest()
sha=hashlib.sha256(text.encode()).hexdigest()

print("MD5 :",md5)
print("SHA :",sha)


print("\n3. Base64 Encoding/Decoding")

encoded=base64.b64encode(text.encode()).decode()
decoded=base64.b64decode(encoded).decode()

print("Base64 encoded :",encoded)
print("Base64 decoded :",decoded)