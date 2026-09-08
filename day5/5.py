#linked list is a form of sequential collection
#and it does not have to be in order 
#a linked list is made up of independent nodes that
#may contain any type of data and 
#each node has a reference to the next node in the link 

class Node:
    def __init__(self,value):#head
        self.data=value#[10|102]--[20|103]--[30|null]
        self.next=None#101

class LinkedList:
    def __init__(self):
        self.head=None#None

linkedobj = LinkedList()
    #creating independent node 
linkedobj.head = Node(10)
second         = Node(20)
third          = Node(30)
fourth         = Node(40)

linkedobj.head.next = second
second.next=third
third.next=fourth

#display linked list
while linkedobj.head !=None:
    print("[",linkedobj.head.data,"|",linkedobj.head.next,"]","->",end="")
    linkedobj.head = linkedobj.head.next