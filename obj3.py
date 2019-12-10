class Person:
    def __init__(self, n, a):
        self.name=n
        self.age= a
    def display(self):
        print ("Name :", self.name)
        print ("Age :", self.age)

class Student (Person):
    def __init__(self, n, a, r, b):
        super().__init__(n,a)
        self.rollno= r
        self.branch=b

    def display(self):
        super().display()
        print("Rollno :", self.rollno)
        print("Branch :", self.branch)

class Employee (Person):
    pass

s1= Student ("Kumar", 24, "123", "CS")
s1.display()