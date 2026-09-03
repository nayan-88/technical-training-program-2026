#why python is dynamically typed language 
math =50
phy=60.56
chem=70
name="axyz"
print(type(math))
print(type(chem))
print(type(phy))
print(type(name))
#how to check address in var
# id() check adresses of variable
print(id(math))
print(id(chem))
print(id(phy))
print(id(name))



num=123456
a=num%10
num=num//10
b=num%10
num=num//10
c=num%10
num=num//10
d=num%10
num=num//10
e=num%10
f=num//10
rev=a*100000+b*10000+c*1000+d*100+e*10+f*1
print(rev)