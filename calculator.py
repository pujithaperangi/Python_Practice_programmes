#simple calculator
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

def operation(a,b,oper):
    if oper=="+":
         return a+b
    elif oper=="-":
        return a-b
    elif oper=="*":
        return a*b
    elif oper=="/":
        return a/b
    else:
        return 0


a=int(input("first number :"))

oper=input("operations : + - * /")

b=int(input("second number :"))

cal=operation(a,b,oper)
print(cal)

flag=input("do u want ot continue with the computation with the result -> s or n")
while flag=="s":
    oper = input("operations : + - * /")
    b = int(input("second number :"))
    a,b=cal,b
    cal=operation(a,b,oper)
    print(cal)
    flag = input("do u want ot continue with the computation with the result -> s or n")



