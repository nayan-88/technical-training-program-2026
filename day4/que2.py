# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i,end=" ")
#     print()

# ----------------------------------------

# n=int(input("Enter the number of rows: "5))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(64+j),end=" ")
#     print()
# ----------------------------------------

# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(n+1-i,end=" ")
#     print()
# ----------------------------------------
# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("*",end=" ")
#     print()


# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     print(""*(n-i),end="")
#     for j in range(1,i+1):
#         print("*",end=" ")
        
        
#     print()


# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     print(""*(n-i),end="")
#     for j in range(1,i+1):
#         print(chr(64+i),end=" ")
# print()

# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     print(""*(n-i),end="")
#     for j in range(1,i):
#         print(i-j,end=" ")
#     for k in range(0,i):
#         print(k,end=" ")
#     print()

# print('subject marks:')
# phy =50
# chem = 60 
# math = 70

# print("physice={} chem={} math={}".format(phy,chem,math))
# print("physice={0} chem={1} math={2}".format(phy,chem,math))
# print("physice={x} chem={y} math={z}".format(x=phy, y=chem, z=math))
# total = phy + chem + math
# print("total marks",f"{total}")
# print("roll no=","7".zfill(4)) 


# s = "Python is High level programing Language"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())


# s = "prashant","ashish","sandip"
# m = '-'.join(s)
# print(m)

# s = "help4code is a best pltform for practicing programming"

# print(s.find("help4code"))
# print(s.find("python"))
# print(s.find("programming"))


# print('nayan7777'.isalnum())
# print('sbsnhgn7777'.isalpha())
# print('gbbgb7777'.isdigit())
# print('ddsb7777'.islower())
# print(''.islower())
# print('nayan7777'.isupper())
# print('my name is nayan'.istitle())
# print(''.istitle())
# print(''.isspace())
# print('nayan7777'.startswith('nayan'))
# print('nayan7777'.endswith('7777'))

# name = "nayan"

# print(name[0])
# print(name[1])
# print(name[-1])
# print(name[0:4])
# print(name[2:])
# print(name[:4])

name = "nayan"
for i in range(len(name)-1,-1,-1):
    print(name[i],end="")   

name = "nayan"
result = ""

for i in range(len(name)-1, -1, -1):
    if name[i] not in result:
        result += name[i]

print(result)