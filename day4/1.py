# A class is a blueprint used to create Student objects.
class Student:
    # __init__ is the constructor. Python calls it automatically each time
    # a new Student object is created.
    def __init__(self):
        # This message is printed when the constructor runs.
        print('i will called automatically')
    def message(self):
        print('Hello inside a class')
# IMPORTANT: Student() creates an object and immediately executes __init__.
obj = Student()
obj2 = Student()

# IMPORTANT: Printing an object without a custom __str__ method shows its
# default representation, which includes the class name and a memory address.
print(obj)
obj.message()
