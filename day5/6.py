class Node:
    def __init__(self,value):
        self.data = value#[10|none]
        self.next=None#101

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    def addNodeBeginning(self,value):
        nodevalue = Node(value)
        if self.head is None:
            self.head = nodevalue
            self.tail = nodevalue
        else:
            nodevalue.next=self.head
            self.head = nodevalue

    def addNodeEnd(self,value):
        nodeValue = Node(value)
        if self.head is None:
            self.head = nodeValue
            self.tail = nodeValue
        else:
            self.tail.next = nodeValue
            self.tail = nodevalue


    def display(self):
        temp = self.head
        while self.head !=None:
            print("[",self.head.data,"]","->",end="")
            temp= temp.next
   
linked_obj=Linkedlist

linked_obj.addNodeBeginning(10)
linked_obj.addNodeBeginning(5)
linked_obj.addNodeEnd(5)
linked_obj.addNodeEnd(6)
linked_obj.display()