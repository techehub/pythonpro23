import random
def outer (a, b):
    c= random.randint(10,100)
    print (c)
    def inner ():
        return a+b+c
    return inner

sum1 = outer (100,100)
sum2 = outer (200, 200)

print (sum2 ())
print (sum1 ())