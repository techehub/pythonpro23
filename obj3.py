class Person:
    def __init__(self, n, a):
        self.__name=n
        self._age= a
    def display(self):
        print ("Name :", self.__name)


class Student (Person):
    def __init__(self, n, a, r, b):
        super().__init__(n,a)
        self.rollno= r
        self.branch=b

    def display(self):
        super().display()
        print("Age :", self._age)
        print("Rollno :", self.rollno)
        print("Branch :", self.branch)

class Employee (Person):
    pass

s1= Student ("Kumar", 24, "123", "CS")
s1._Person__name="Kabeer"
s1.display()

print (s1.__dict__)
