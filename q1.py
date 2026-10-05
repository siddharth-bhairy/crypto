text=input("enter the plain text : ")

key=int(input("enter caesar key : "))

print("1. Caesar Cipher")

result=""

for ch in text:
    if ch.isalpha():
        if ch.isupper():
            result+=chr((ord(ch)-65+key)%26+65)
        else:
            result+=chr((ord(ch)-97+key)%26+97)
    else:
        result+=ch

print("Caesar Cipher :",result)


print("2. Modified Caesar Cipher")

result=""

for ch in text:
    if ch.isalpha():
        if ch.isupper():
            x=ord(ch)-65
            result+=chr((x+5)%26+65)
        else:
            x=ord(ch)-97
            result+=chr((x+5)%26+97)
    else:
        result+=ch

print("Modified Caesar Cipher :",result)


print("3. Playfair Cipher")

playfair_key=input("enter playfair key : ").replace(" ","").upper()

plain=text.replace(" ","").upper()
playfair_key=playfair_key.replace("J","I")
plain=plain.replace("J","I")

used=""

for ch in playfair_key:
    if ch.isalpha() and ch not in used:
        used+=ch

for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
    if ch not in used:
        used+=ch

matrix=[]

for i in range(0,25,5):
    matrix.append(used[i:i+5])

pairs=[]
i=0

while i<len(plain):
    a=plain[i]

    if i+1<len(plain):
        b=plain[i+1]
    else:
        b="X"

    if a==b:
        pairs.append(a+"X")
        i+=1
    else:
        pairs.append(a+b)
        i+=2

result=""

for pair in pairs:

    a=pair[0]
    b=pair[1]

    r1=c1=r2=c2=0

    for i in range(5):
        for j in range(5):
            if matrix[i][j]==a:
                r1=i
                c1=j

            if matrix[i][j]==b:
                r2=i
                c2=j

    if r1==r2:
        result+=matrix[r1][(c1+1)%5]
        result+=matrix[r2][(c2+1)%5]

    elif c1==c2:
        result+=matrix[(r1+1)%5][c1]
        result+=matrix[(r2+1)%5][c2]

    else:
        result+=matrix[r1][c2]
        result+=matrix[r2][c1]

print("Playfair Cipher :",result)