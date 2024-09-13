#ceasar cipher is the simplest cipher technique in the cryptographic network system
alp="abcdefghijklmnopqrstuvwxyz"
def encrypt(string,n):
    encrp=""
    prev_space = False
    for i in string:
        if i == " ":
            if not prev_space:
                encrp += " "
                prev_space = True
        else:
            prev_space = False
            for j in range(26):
                if i==" ":
                    encrp+=" "
                if i==alp[j]:
                    k=(j+n)%26
                    encrp+=alp[k]

    print(encrp)





def decrypt(string,n):
    decrp = ""
    prev_space = False
    for i in string:
        if i == " ":
            if not prev_space:
                decrp += " "
                prev_space = True
        else:
            prev_space = False
            for j in range(26):
                if i == " ":
                    decrp += " "
                if i == alp[j]:
                    k = (j - n) % 26
                    if k <0 :
                        k+=26
                    decrp += alp[k]

    print(decrp)



#global alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']



flag="s"
while flag=="s":
    choice = input("type 'en' if u want ot encrypt the message or 'dec' to decrypt the message").lower()
    string = input("ur string :").lower()
    n = int(input("step :"))
    if choice=="en":
        encrypt(string, n)
    elif choice=="dec":
        decrypt(string,n)
    else:
        print("invalid")

    flag=input("if u want to continue then type 's'  or else 'n'")

else:
    print("Bye")
