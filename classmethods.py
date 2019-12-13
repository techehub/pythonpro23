import random

class Student :
    def __init__(self, id, name, mark1, mark2, mark3):
        self.id = id
        self.name = name
        self.mark1=mark1
        self.mark2= mark2
        self.mark3 =mark3

    def totalMark (self):
        return self.mark1+ self.mark2 + self.mark3

    @staticmethod
    def avg (total , count):
        return  total/count

    @staticmethod
    def createId ():
        return  random.randint(10000, 20000)

    @classmethod
    def createStudent (cls, data):
        id = Student.createId()
        obj =cls (id,
                  data ['name'],
                  data ['sub1'],
                  data ['sub2'],
                  data ['sub3'])

        return obj
