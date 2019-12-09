class Student :
    def __init__(self,  name, rollno, marks):
        self.rollno= rollno
        self.name= name
        self.marks= marks.split (",")
        print ("Object created ")

    def totalMarks(self):
        return int (self.marks[0])+\
               int (self.marks[1]) + \
               int (self.marks[2])

    def avgMarks (self):
        return self.totalMarks()/3

    def display (self):
        print ("Roll No: " ,self.name)
        print("Name: ", self.name)
        print("Total: ", self.totalMarks())
        print("Avg Mark: ", self.avgMarks())

i= 0
students = []
c = input ("Number of students ::")
while  (i<int(c)):
    name = input ("Name :" )
    rollno = input("RollNo :")
    marks  = input ("Mark (in coma separated) :")
    s1 = Student (name, rollno, marks)
    students.append(s1)
    i= i+1



for x in students :
    x.display()