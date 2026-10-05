p=int(input("enter prime number: "))
g=int(input("enter primitive root: "))

a=int(input("enter private key of A: "))
b=int(input("enter private key of B: "))

A=(g**a)%p
B=(g**b)%p

key1=(B**a)%p
key2=(A**b)%p

print("Public key of A:",A)
print("Public key of B:",B)

print("Secret key of A:",key1)
print("Secret key of B:",key2)

if key1==key2:
    print("Key exchange successful")
else:
    print("Key exchange failed")