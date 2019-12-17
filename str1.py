class Student:
    def __init__(self, id, name, age):
        self.id= id
        self.name=name
        self.age= age

    def __str__(self):
           return self.id + ":" + self.name


s1= Student("123", "kumar", 23)
print (s1)

