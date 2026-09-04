def add(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

def mul(a,b):
    print(a*b)

def div(a,b):
    print(a/b)

while True:
    print("1.Addition")
    print("2.sub")
    print("3.mul")
    print("4.div")
    print("5,exit")
    choice = int(input("enter your choice:"))
    if choice == 1:
        add(5,5)
    elif choice == 2:
        sub(5,5)
    elif choice == 3:
         mul(5,5)
    elif choice == 4:
        div(5,5)
    else:
        break