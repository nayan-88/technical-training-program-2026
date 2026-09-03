cha=ord(input("enter a value:"))
if cha>=65 and cha<=90:
    print("upper case")
elif cha>=97 and cha <=122:
    print("lower case")

elif cha>=48 and cha<=57:
    print("dizit")
else:
    print("special charcter")


mylist = [2,4,6,8,9,1,5]
#slicing of list 
print(mylist [0])
print(mylist [2])
print(mylist [1:])#
print(mylist [1:5])#4,6,8,9
print(mylist[0:6:2])
print(mylist[::-1])
