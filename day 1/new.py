math=int(input("entre a marks:"))
sci=int(input("enter a second  marks:"))
phy=int(input("enter a tgird marks:"))

total=math+sci+phy
print("total marks is :",total)

per=total/3.0
print(per)

if math>=40 and sci>=40 and phy>=40:
    print("pass")
else:
    print("fail")

if per>=60 and total>=100:
    print("you are eligible for placement:")
else:
    print("not eligible fro placement")