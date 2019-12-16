def outer (f):
    def inner (*a, **b):
        print ("%%%%%%%%%%")
        print (a)
        print (b)
        f (*a, **b)
        print ("%%%%%%%%%%")
    return inner

@outer
def add (x, y):
    print ( x+y)

@outer
def hai ():
    print ("Hello")

@outer
def greet (phone, **val):
    print  (phone, val["msg"] + "," + val["name"])

def diff (x,y):
    print ( x-y)


greet ("2132342", name="Kumar", msg="Good morning")

'''
add (10,10)
calc1 = outer (add)
calc1(10,10)
'''