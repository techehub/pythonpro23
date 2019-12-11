class Student :
    def __init__ (self,name, mark):
        self.name =name
        self.mark = mark

    def __add__(self, other):
        return Student (self.name + ","+other.name , self.mark + other.mark)

    def __gt__(self, other):
        return self.mark > other.mark


s1= Student ("anil", 600)
s2= Student ("seetha", 540)
s3= Student ("kumar", 540)
s4= Student ("anil", 600)
s5= Student ("seetha", 540)
s6= Student ("kumar", 540)

students = [s1, s2, s3, s4, s5,s6]
s= Student ("", 0)
for x in students :
    s = s +  x

print (s.name)
print (s.mark)
