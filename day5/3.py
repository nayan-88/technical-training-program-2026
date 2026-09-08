#static variables and methods
class College:
    college_Name = "ABC College"  # static variable

obj1 = College()
obj2 = College()
obj3 = College()
print(obj1.college_Name)
print(obj2.college_Name)
print(obj3.college_Name) # accessing static variable using class name
College.college_Name = "XYZ College" # changing static variable using class name
print(obj1.college_Name)
print(obj2.college_Name)
print(obj3.college_Name) # accessing static variable using class name