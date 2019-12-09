class Student :
    def __init__(self, rollno, name):
        self.rollno= rollno
        self.name= name
        print ("Object created ")

    def totalMarks(self):
        return self.marks[0]+\
               self.marks[1] + \
               self.marks[2]

    def avgMarks (self):
        return self.totalMarks()/3

    def display (self):
        print ("Roll No: " ,self.name)
        print("Name: ", self.name)
        print("Total: ", self.totalMarks())
        print("Avg Mark: ", self.avgMarks())


s1 = Student ("111", "Ramu")
s2 = Student ("222", "Somu")

s1.marks= [22,33,44]
s2.marks= [11,12,13]

s1.display()
s2.display()
