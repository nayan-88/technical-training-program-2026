#stck using list
#easy to implement , speed problem when it grows
#stack using linked list
#fast performance, but more complex to implement

import sys
class Stack:
    def __init__(self, stackSize):
        # Store the size passed when the Stack object is created.
        self.stackSize = stackSize
        self.stackList = []

    def isFull(self):
        if len(self.stackList) == self.stackSize:
            return True
        else:
            return False
    def isEmpty(self):
        if self.stackList == []:
            return True
        else:
            return False
    def push(self, data):
        if self.isFull():
            print("Stack is full")
        else:
            self.stackList.append(data)

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print(self.stackList.pop())

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print(self.stackList[-1])
    def deleteStack(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            self.stackList = None
            print("Stack deleted successfully")

    def display(self):
        print(self.stackList) 
size = int(input("Enter the size of stack: "))
objStack=Stack(size)

while True:
    print("1. Push element")
    print("2. Pop element")
    print("3. Peek element")
    print("4. Display elements")
    print("5. isEmpty ")
    print("6. isFull ") 
    print("7. Delete Stack ")
    print("8. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        value = int(input("Enter the value to push: "))
        objStack.push(value)
    elif choice == 2:
        objStack.pop()
    elif choice == 3:
        objStack.peek()
    elif choice == 4:
        objStack.display()
    elif choice == 5:
         print(objStack.isEmpty())
    elif choice == 6:
         print(objStack.isFull())
    elif choice == 7:
        objStack.deleteStack()
    elif choice == 8:
        sys.exit()

    
    
