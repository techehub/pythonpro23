from files.classmethods import Student

data = { "name": "Kumar",
         "sub1": 22, "sub2":33, "sub3":44}


s1 = Student.createStudent(data)

id = Student.createId()
s2 = Student(id, "anil", 44, 66, 77)

print (s1.totalMark())
print (s2.totalMark())

print (Student.avg(500,5))