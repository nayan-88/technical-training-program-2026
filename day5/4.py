class College:
    college_Name = "ABC College"  # static variable
    def __init__(self):
        self.studentname = "nayan raut" # instance variable(3 separate instance variables)

principal = College()
teacher = College()
accountant = College()
print("principal=", principal.collegeName,"....",principal.studentname)
print("teacher =",teacher.collegeName,"....",teacher.studentname)
print(" accountant=",accountant.collegeName,"....",accountant.studentname)

College.college_Name="HBD"
principal.studentname="prashant jha"

print("principal=", principal.collegeName,"....",principal.studentname)
print("teacher =",teacher.collegeName,"....",teacher.studentname)
print("accountant=",accountant.collegeName,"....",accountant.studentname)

