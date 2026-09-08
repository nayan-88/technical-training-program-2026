#accessing and deleting instance variable from the class
class Student:
    def __init__(self):
        self.name = input("Enter your name: ")#instance variable
        self.s_rollno = 101

    def getdata(self):
        self.s_mb = 28493882928 #instance variable

obj = Student()
obj.getdata()
obj.s_branch = "CS"#adding insance variable by using object
del obj.s_rollno#deleting a instance variable from the class
print(obj.__dict__)
