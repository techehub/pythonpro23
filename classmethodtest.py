from files.classmethods import Student


data = { "name": "Kumar",
         "sub1": 22, "sub2":33, "sub3":44}
s1 = Student.createStudent(data)

print (s1.totalMark())