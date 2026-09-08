class Employee:
    def __init__(self):
        self.name = "nayan raut"

obj1 = Employee()
obj2 = Employee()
obj3 = Employee()

print(obj1.name)
print(obj2.name)
print(obj3.name)

obj1.name = "nayan"
obj2.name = "raja"
print(obj1.name)
print(obj2.name)
print(obj3.name)
