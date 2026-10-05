text=input("enter the plain text : ")

print("1. Rail Fence Technique")

rails=int(input("enter number of rails : "))

text=text.replace(" ","")

matrix=[["" for j in range(len(text))] for i in range(rails)]

row=0
direction=1

for i in range(len(text)):
    matrix[row][i]=text[i]

    if row==0:
        direction=1
    elif row==rails-1:
        direction=-1

    row+=direction

result=""

for i in range(rails):
    for j in range(len(text)):
        if matrix[i][j]!="":
            result+=matrix[i][j]

print("Rail Fence Cipher :",result)


print("2. Columnar Technique")

key=input("enter columnar key : ").replace(" ","").upper()

text=text.upper()

cols=len(key)
rows=(len(text)+cols-1)//cols

matrix=[]

k=0

for i in range(rows):
    row=[]

    for j in range(cols):
        if k<len(text):
            row.append(text[k])
            k+=1
        else:
            row.append("X")

    matrix.append(row)

order=sorted(range(cols),key=lambda x:key[x])

result=""

for j in order:
    for i in range(rows):
        result+=matrix[i][j]

print("Columnar Cipher :",result)