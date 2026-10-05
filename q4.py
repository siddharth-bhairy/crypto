import rsa

username=input("enter username : ")
password=input("enter password : ")

public_key,private_key=rsa.newkeys(512)

encrypted=rsa.encrypt(password.encode(),public_key)
decrypted=rsa.decrypt(encrypted,private_key).decode()

print("username -",username)
print("password -",password)
print("encrypted password -",encrypted)
print("decrypted password -",decrypted)