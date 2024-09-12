#easy
import random
alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Alp=[letter.upper() for letter in alp]

print("Welcome to password generator :)")
leth=int(input("length of password :"))
a=int(input("no.of  small alphabets"))
A=int(input("no.of  capital alphabets"))
s=int(input("no.of special characters"))
n=int(input("no.of numbers"))
special=["!","@","#","$","%","^","&","*","(",")","_","-","+","=",",",".","?","/","|"]
num=["0","1","2","3","4","5","6","7","8","9"]
pwd=[]

if a + A + s +n != leth:
    print("Error: The sum of characters doesn't match the password length!")
else:
    for j in range(a):
        pwd.append(random.choice(alp))

    for k in range(s):
        pwd.append(random.choice(special))

    for z in range(A):
        pwd.append(random.choice(Alp))

    for b in range(n):
        pwd.append(random.choice(num))



random.shuffle(pwd)

for i in pwd:
    print(i,end="")


