class Student (object):
    def __init__(self):
        print ("Student Object created !!")
    def total(a):
        return a.marks[0]+\
               a.marks[1] + \
               a.marks[2]


ramu= Student()
somu = Student()

ramu.rollno = "123"
ramu.name= "Ram Kumar"
ramu.marks= [11,33,44]


somu.rollno= "111"
somu.name= "Somu"
somu.marks= [33,32,4]
somu.phone= "7863473284"


print (ramu.total())
print (somu.total())