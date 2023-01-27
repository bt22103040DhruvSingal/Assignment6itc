class Student:
    def Student():
        return self
class Marks:
    def Marks():
        return self
m = Marks()
s = Student()
if type(m) == Marks:
    print("Object m  belongs to class marks")
if type(s) == Student:
    print("Object s belongs to class Students")
    
if issubclass(Student,object):
    print("Class Students is a sub class of class Object")
if issubclass(Marks,object):
    print("Class Marks is a sub class of class Object")
