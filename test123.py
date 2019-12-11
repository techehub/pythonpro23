

class Student :
    def __init__ (self,name):
        self.name =name


s1 = Student ("kumar")

print (hasattr(s1,"name"))
print (getattr(s1,"name"))
setattr(s1, "name", "anand")
print (getattr(s1,"name"))
delattr(s1,"name")
print (hasattr(s1,"name"))



